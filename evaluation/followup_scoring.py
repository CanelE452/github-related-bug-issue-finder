"""Version 2 scoring of immutable retrieval records. No relevance labels are inferred."""
import csv
import math
from collections import defaultdict
from datetime import datetime
from pathlib import Path

from backend.app.storage import digest


def csv_rows(path):
    with Path(path).open(encoding='utf-8-sig',newline='') as f:
        result=list(csv.DictReader(f))
    for row in result:
        for key in ['evidence_quote','reason','reviewer_id']:
            value=row.get(key,'')
            if value.startswith("'") and value[1:].lstrip().startswith(('=','+','-','@')):row[key]=value[1:]
    return result


def provenance(row):
    if row.get('reviewer_type')!='human' or not row.get('reviewer_id') or not row.get('reviewed_at') or not row.get('reason'):
        raise ValueError('Actual human provenance/time/reason required; identity is not authenticated by software')
    timestamp=datetime.fromisoformat(row['reviewed_at'].replace('Z','+00:00'))
    if timestamp.tzinfo is None: raise ValueError('reviewed_at requires timezone')


def resolve_reviews(pool, queries, document_texts, document_urls, review_rows, query_rows, adjudications=()):
    adjudications=list(adjudications)
    expected={r['review_item_id']:r for r in pool};query_groups=defaultdict(list);doc_groups=defaultdict(list)
    seen=set();people=set();accepted_records=[]
    for row in query_rows:
        qid=row.get('query_id')
        if qid not in queries or row.get('query_sha256')!=queries[qid]['query_sha256']:
            raise ValueError('query ID/content hash mismatch')
        if row.get('review_status') not in {'reviewed','rejected'}: continue
        provenance(row);key=('query',qid,row['reviewer_id'])
        if key in seen: raise ValueError('duplicate reviewer/query; submit one current version per reviewer')
        seen.add(key);people.add(row['reviewer_id']);accepted_records.append(dict(row))
        if row['review_status']=='reviewed' and any(row.get(k) not in {'yes','no'} for k in ['symptom_faithful','no_solution_leakage','information_change_checked']):
            raise ValueError('query contract answers required')
        query_groups[qid].append(row)
    for row in review_rows:
        rid=row.get('review_item_id');ref=expected.get(rid)
        if not ref or any(row.get(k)!=ref[k] for k in ['query_id','doc_id','query_sha256','document_sha256']):
            raise ValueError('review item/query/document ID or hash mismatch')
        if row.get('review_status')!='reviewed':continue
        provenance(row);key=('document',rid,row['reviewer_id'])
        if key in seen:raise ValueError('duplicate reviewer/item; independent reviews must not overwrite')
        seen.add(key);people.add(row['reviewer_id']);accepted_records.append(dict(row))
        if row.get('evidence_scope') not in {'title_body','comment_only','unavailable'} or row.get('condition_relation') not in {'supports','conflicts','unknown','not_applicable'}:
            raise ValueError('invalid scope/condition relation')
        if row['evidence_scope']=='unavailable':
            if row.get('grade','') not in ('',None):raise ValueError('unavailable is unjudged, not a numeric grade')
        else:
            if row.get('grade') not in {'0','1','2'} or not row.get('evidence_quote') or not row.get('evidence_url'):
                raise ValueError('numeric grade and actual evidence required')
            if row['evidence_url'].split('#')[0]!=document_urls[ref['doc_id']]:raise ValueError('evidence URL does not identify reviewed document')
            if row['evidence_scope']=='title_body' and ' '.join(row['evidence_quote'].split()) not in ' '.join(document_texts[ref['doc_id']].split()):
                raise ValueError('evidence quote absent from frozen title/body')
        doc_groups[rid].append(row)
    resolutions={}
    for row in adjudications:
        provenance(row);kind=row.get('kind');key=row.get('target_id')
        if (kind,key) in resolutions:raise ValueError('duplicate adjudication')
        if kind=='query':
            if key not in queries or row.get('query_sha256')!=queries[key]['query_sha256'] or row.get('approved') not in {'yes','no'}:
                raise ValueError('invalid query adjudication')
        elif kind=='document':
            ref=expected.get(key)
            if not ref or any(row.get(k)!=ref[k] for k in ['query_id','doc_id','query_sha256','document_sha256']):raise ValueError('invalid document adjudication IDs/hashes')
            if row.get('grade') not in {'0','1','2'} or row.get('evidence_scope')!='title_body' or not row.get('evidence_quote') or row.get('evidence_url','').split('#')[0]!=document_urls[ref['doc_id']]:raise ValueError('adjudication needs frozen title/body evidence')
            if ' '.join(row['evidence_quote'].split()) not in ' '.join(document_texts[ref['doc_id']].split()):raise ValueError('adjudication quote absent')
        else:raise ValueError('invalid adjudication kind')
        resolutions[(kind,key)]=row;people.add(row['reviewer_id'])
    approval={};qrels=[]
    for qid in queries:
        records=query_groups[qid];votes=[r['review_status']=='reviewed' and all(r.get(k)=='yes' for k in ['symptom_faithful','no_solution_leakage','information_change_checked']) for r in records]
        adj=resolutions.get(('query',qid))
        approved=adj['approved']=='yes' if adj else bool(votes) and all(votes)
        reason='adjudicated' if adj else 'query_unreviewed' if not votes else 'query_rejected' if not any(votes) else 'query_reviewer_disagreement' if not all(votes) else 'approved'
        approval[qid]={'approved':approved,'reason':reason,'reviewers':len(records),'exposure':[r.get('exposure','not_provided') for r in records]}
    for rid,ref in expected.items():
        records=doc_groups[rid];adj=resolutions.get(('document',rid))
        values=[int(r['grade']) if r.get('grade') in {'0','1','2'} and r['evidence_scope']=='title_body' else None for r in records]
        grade=int(adj['grade']) if adj else values[0] if values and None not in values and len(set(values))==1 else None
        reason='adjudicated' if adj else 'unreviewed' if not values else 'evidence_unavailable_or_comment_only' if None in values else 'reviewer_disagreement' if len(set(values))>1 else 'reviewed'
        evidence=[adj] if adj else records
        qrels.append({**{k:ref[k] for k in ['review_item_id','query_id','doc_id','query_sha256','document_sha256']},
                      'grade':grade,'reason':reason,'reviewers':len(records),'evidence':[dict(r) for r in evidence]})
    return {'approval':approval,'qrels':qrels,'human_reviewers':len(people),'single_human_reviewer':len(people)==1,
            'independent_records':accepted_records,'adjudications':[dict(r) for r in adjudications]}


def query_metrics(top_ids, judgments, pool_ids, query_approved, status='ok'):
    complete=all(judgments.get(d) in (0,1,2) for d in pool_ids)
    confirmed=1 if query_approved and any(judgments.get(d)==2 for d in top_ids[:5]) else None
    result={'confirmed_hit':confirmed,'pool_complete':complete,'hit_at_5':None,'pooled_ndcg_at_5':None,'reason':None}
    if status=='execution_error':result.update(confirmed_hit=None,reason='execution_error');return result
    if not query_approved:result['reason']='query_not_approved';return result
    if not complete:result['reason']='common_pool_incomplete';return result
    if any(d not in pool_ids for d in top_ids[:5]):raise ValueError('Top-5 outside common pool; expand pool before scoring')
    result['hit_at_5']=1 if any(judgments[d]==2 for d in top_ids[:5]) else 0
    gains=sorted((2**judgments[d]-1 for d in pool_ids),reverse=True)[:5]
    ideal=sum(g/math.log2(i+2) for i,g in enumerate(gains))
    if not ideal:result['reason']='idcg_zero';return result
    result['pooled_ndcg_at_5']=sum((2**judgments[d]-1)/math.log2(i+2) for i,d in enumerate(top_ids[:5]))/ideal
    return result


def extend_pool(pool, runs, queries, hashes):
    result={(x['query_id'],x['doc_id']):dict(x) for x in pool}
    for run in runs:
        qid=run['query_id']
        for item in run['ranked_results'][:5]:
            did=item['doc_id']
            result.setdefault((qid,did),{'review_item_id':digest([qid,did])[:16],'query_id':qid,'doc_id':did,
                                       'query_sha256':queries[qid]['query_sha256'],'document_sha256':hashes[did]})
    return sorted(result.values(),key=lambda r:(r['query_id'],r['doc_id']))


def score_records(runs, queries, cases, pool, resolved, scope_ids):
    core=[r for r in runs if r['kind']=='core'];core_ids={r['query_id'] for r in core}
    cells=defaultdict(set)
    for r in core:cells[(r['method'],r['corpus_scope'])].add(r['query_id'])
    if not core_ids or any(ids!=core_ids for ids in cells.values()):raise ValueError('methods/scopes must share the same core query universe')
    expected=defaultdict(set);grades=defaultdict(dict)
    for row in pool:expected[row['query_id']].add(row['doc_id'])
    for row in resolved['qrels']:grades[row['query_id']][row['doc_id']]=row['grade']
    if any(not expected[q] for q in core_ids):raise ValueError('each core query needs a frozen common pool')
    complete={q for q in core_ids if resolved['approval'].get(q,{}).get('approved') and all(grades[q].get(d) is not None for d in expected[q])}
    errors={r['query_id'] for r in core if r['status']=='execution_error'}
    comparable=complete-errors
    qrels_version=digest(resolved['qrels']);pool_version=digest(pool);by_query=[]
    for r in core:
        qid=r['query_id'];approved=resolved['approval'][qid]['approved'];values=query_metrics([x['doc_id'] for x in r['ranked_results']],grades[qid],expected[qid],approved,r['status'])
        by_query.append({**{k:r[k] for k in ['query_id','case_id','method','repository','corpus_scope','status']},
                         'variant':queries[qid]['variant'],'stratum':cases[r['case_id']]['stratum'],
                         'query_approved':approved,'common_comparison_eligible':qid in comparable,'pool_version':pool_version,'qrels_version':qrels_version,**values})
    summaries=[]
    groups={(r['method'],r['corpus_scope'],r['variant'],repo,stratum) for r in by_query
            for repo,stratum in [('ALL','ALL'),(r['repository'],'ALL'),(r['repository'],r['stratum'])]}
    for method,scope,variant,repo,stratum in sorted(groups):
        subset=[r for r in by_query if r['method']==method and r['corpus_scope']==scope and r['variant']==variant
                and (repo=='ALL' or r['repository']==repo) and (stratum=='ALL' or r['stratum']==stratum)]
        eligible=[r for r in subset if r['common_comparison_eligible']];ndcg=[r for r in eligible if r['pooled_ndcg_at_5'] is not None]
        positive=[r for r in eligible if any(g==2 and d in scope_ids[(r['repository'],scope)] for d,g in grades[r['query_id']].items())]
        summaries.append({'method':method,'scope':scope,'variant':variant,'repository':repo,'stratum':stratum,
                          'planned_n':len(subset),'approved_n':sum(r['query_approved'] for r in subset),
                          'pool_complete_n':sum(r['pool_complete'] and r['query_approved'] for r in subset),
                          'execution_error_n':sum(r['status']=='execution_error' for r in subset),'comparison_n':len(eligible),
                          'common_query_ids_hash':digest(sorted(r['query_id'] for r in eligible)),
                          'hit_at_5':sum(r['hit_at_5'] for r in eligible)/len(eligible) if eligible else None,
                          'ndcg_n':len(ndcg),'pooled_ndcg_at_5':sum(r['pooled_ndcg_at_5'] for r in ndcg)/len(ndcg) if ndcg else None,
                          'known_positive_n':len(positive),'hit_at_5_known_available':sum(r['hit_at_5'] for r in positive)/len(positive) if positive else None,
                          'pool_version':pool_version,'qrels_version':qrels_version,'reason':None if eligible else 'no_common_completed_queries'})
    state='REVIEWED' if len(complete)==len(core_ids) else 'PARTIALLY_REVIEWED' if resolved['human_reviewers'] else 'AWAITING_HUMAN_REVIEW'
    return {'by_query':by_query,'summary':summaries,'pool_version':pool_version,'qrels_version':qrels_version,
            'state':state,'planned_queries':len(core_ids),'approved_queries':sum(resolved['approval'][q]['approved'] for q in core_ids),
            'complete_queries':len(complete),'comparison_queries':len(comparable),'core_families':len({r['case_id'] for r in core}),
            'pool_pairs':len(pool),'judged_pairs':sum(q['grade'] is not None for q in resolved['qrels']),
            'human_reviewers':resolved['human_reviewers'],'single_human_reviewer':resolved['single_human_reviewer']}
