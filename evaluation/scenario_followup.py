"""Read-only parent audit, offline human review and versioned rescoring CLI."""
import argparse
import csv
import json
import platform
import shutil
import sys
from pathlib import Path

from backend.app.config import ROOT
from backend.app.domain import issue_text, query_text
from backend.app.storage import digest
from evaluation.scenario_eval import read, rows, sha_file, now, corpus
from evaluation.followup_review import package, QUERY_FIELDS, DOCUMENT_FIELDS
from evaluation.followup_scoring import csv_rows, resolve_reviews, score_records

CONFIG = ROOT/'evaluation/scenario_followup_v2/config.json'


def save(path, value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')


def save_rows(path, records):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in records),encoding='utf-8',newline='\n')


def save_csv(path, records, fields=None):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    if fields is None:fields=list(records[0]) if records else []
    with path.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,lineterminator='\n',extrasaction='ignore');w.writeheader()
        for r in records:
            # Protect exported evidence from spreadsheet formulas, leaving source data unchanged.
            values={k:json.dumps(v,ensure_ascii=False) if isinstance(v,(dict,list)) else v for k,v in r.items()}
            w.writerow({k:("'"+v if isinstance(v,str) and v.lstrip().startswith(('=','+','-','@')) else v) for k,v in values.items()})


def load_parent(parent):
    parent=Path(parent);m=read(parent/'manifest.json')
    if digest(m['config'])!=m['config_hash']:raise ValueError('parent configuration hash changed')
    queries={q['query_id']:q for q in rows(parent/'queries.jsonl')};cases={c['case_id']:c for c in rows(parent/'cases.jsonl')}
    if digest(list(queries.values()))!=m['queries_hash'] or digest(list(cases.values()))!=m['cases_hash']:raise ValueError('parent query/case hash changed')
    for q in queries.values():
        if digest(q['query_text'])!=q['query_sha256'] or query_text(q['problem'],q.get('error',''),q.get('environment',''))!=q['query_text']:raise ValueError('query input mismatch')
    documents={};scopes={};snapshots={}
    for repo,meta in m['snapshots'].items():
        if sha_file(parent/meta['file'])!=meta['file_hash']:raise ValueError('parent source snapshot changed')
        snapshot=read(parent/meta['file']);snapshots[repo]=snapshot
        if snapshot['repository']!=repo:raise ValueError('snapshot repository mismatch')
        for x in snapshot['issues']:
            if 'pull_request' in x:raise ValueError('parent corpus contains pull request')
            documents[f'{repo}#{x["number"]}']=x
        for scope in m['config']['scopes']:scopes[(repo,scope)]=corpus(snapshot,scope,m['config']['bug_labels'])
    for c in cases.values():
        for did in c['source_doc_ids']:
            if did in documents and digest(issue_text(documents[did]))!=c['source_hash']:raise ValueError('case source hash mismatch')
    runs=rows(parent/'runs.jsonl');pool=rows(parent/'review_items.jsonl')
    seen=set()
    for r in runs:
        s=scopes[(r['repository'],r['corpus_scope'])];q=queries[r['query_id']]
        if r['query_sha256']!=q['query_sha256'] or r['corpus_hash']!=s['version'] or r['selected_doc_ids_hash']!=s['ids_hash']:raise ValueError('run input/scope identity mismatch')
        if r['model_revision']!=m['config']['model_revision'] or r['config_hash']!=m['config_hash'] or r['code_hash']!=digest(m['code_hashes']):raise ValueError('retrieval version mismatch')
        key=(r['query_id'],r['method'],r['corpus_scope'],r['kind'])
        if key in seen:raise ValueError('duplicate retrieval condition')
        seen.add(key);allowed={f'{r["repository"]}#{x["number"]}' for x in s['issues']}
        if any(x['doc_id'] not in allowed or x['rank']!=i for i,x in enumerate(r['ranked_results'],1)):raise ValueError('rank/document isolation mismatch')
    keys=set();expected={q:set() for q in queries}
    for r in runs:
        if r['kind']=='core':expected[r['query_id']].update(x['doc_id'] for x in r['ranked_results'][:5]);expected[r['query_id']].update(cases[r['case_id']]['source_doc_ids'])
    for x in pool:
        key=(x['query_id'],x['doc_id'])
        if key in keys or x['review_item_id']!=digest(list(key))[:16] or x['query_sha256']!=queries[x['query_id']]['query_sha256'] or x['document_sha256']!=digest(issue_text(documents[x['doc_id']])):raise ValueError('pool ID/content mismatch')
        keys.add(key)
    if keys!={(q,d) for q,ids in expected.items() for d in ids}:raise ValueError('parent common pool incomplete')
    return {'manifest':m,'queries':queries,'cases':cases,'documents':documents,'snapshots':snapshots,'scopes':scopes,'runs':runs,'pool':pool}


def check_preservation(parent, hashes):
    actual={p.relative_to(parent).as_posix():sha_file(p) for p in Path(parent).rglob('*') if p.is_file()}
    if actual!=hashes:raise ValueError('parent directory changed, including byte-level cache/source files')
    return len(actual)


def audit(args):
    batch=Path(args.out);parent=Path(args.parent_run).resolve();batch.mkdir(parents=True,exist_ok=True)
    if parent.resolve()==batch.resolve() or parent.resolve() in batch.resolve().parents:raise ValueError('child output must be outside immutable parent')
    data=load_parent(parent);m=data['manifest'];hashes={p.relative_to(parent).as_posix():sha_file(p) for p in parent.rglob('*') if p.is_file()}
    if (batch/'parent-preservation.json').exists():check_preservation(parent,read(batch/'parent-preservation.json'))
    else:save(batch/'parent-preservation.json',hashes)
    retrieval_files=[k for k in m['code_hashes'] if k.startswith('backend/app/') or k=='evaluation/scenario_eval.py']
    code_matches={k:sha_file(ROOT/k)==m['code_hashes'][k] for k in retrieval_files}
    lineage={'created_at':now(),'parent_run_id':read(CONFIG)['parent_run_id'],'parent_report_commit':read(CONFIG)['parent_report_commit'],
             'parent_run':parent.relative_to(ROOT).as_posix(),'parent_manifest_sha256':sha_file(parent/'manifest.json'),
             'parent_rankings_file':(parent/'runs.jsonl').relative_to(ROOT).as_posix(),'parent_rankings_sha256':sha_file(parent/'runs.jsonl'),'representation':'local_frozen_snapshots',
             'queries_hash':m['queries_hash'],'cases_hash':m['cases_hash'],'parent_retrieval_code_hashes':m['code_hashes'],
             'retrieval_code_matches':code_matches,'parent_model_revision':m['config']['model_revision'],
             'corpus_hashes':{f'{repo}|{scope}':s['version'] for (repo,scope),s in data['scopes'].items()},
             'selected_doc_ids_hashes':{f'{repo}|{scope}':s['ids_hash'] for (repo,scope),s in data['scopes'].items()},
             'used_file_byte_hashes':{k:hashes[k] for k in ['manifest.json','queries.jsonl','cases.jsonl','runs.jsonl','review_items.jsonl','human_reviews.csv','query_reviews.csv']+[v['file'] for v in m['snapshots'].values()]},
             'preserved_parent_files':len(hashes),'config_hash':sha_file(CONFIG),'review_schema_version':2,
             'environment':{'python':sys.version.split()[0],'platform':platform.platform(),'device':'cpu','threads':4},
             'input_integrity':'VERIFIED','exact_retrieval_version':'VERIFIED' if all(code_matches.values()) else 'BLOCKED_CODE_MISMATCH'}
    if (batch/'lineage.json').exists():
        old=read(batch/'lineage.json');new=dict(lineage);new['created_at']=old['created_at']
        if old!=new:raise ValueError('audit inputs changed; create a separate child batch')
    else:save(batch/'lineage.json',lineage)
    print(json.dumps({'input_integrity':'VERIFIED','preserved_files':len(hashes),'saved_conditions':len(data['runs'])}))


def batch_data(batch):
    batch=Path(batch);lineage=read(batch/'lineage.json');parent=ROOT/lineage['parent_run']
    check_preservation(parent,read(batch/'parent-preservation.json'))
    if sha_file(CONFIG)!=lineage['config_hash']:raise ValueError('frozen child configuration changed')
    data=load_parent(parent);data['parent']=parent;data['lineage']=lineage;return data


def prepare_review(args):
    batch=Path(args.batch);d=batch_data(batch)
    pool=read(batch/'current-pool.json') if (batch/'current-pool.json').exists() else d['pool']
    path=package(batch/'review',d['queries'],d['cases'],pool,d['documents'],read(CONFIG)['seed'])
    for filename,fieldnames,records in [('query_reviews.csv',QUERY_FIELDS,[{'query_id':q['query_id'],'query_sha256':q['query_sha256'],'review_status':'unreviewed'} for q in d['queries'].values()]),
                                       ('human_reviews.csv',DOCUMENT_FIELDS,[{**x,'grade':'','reviewer_type':'','reviewer_id':'','reviewed_at':'','review_status':'unreviewed','reason':'','evidence_quote':''} for x in pool])]:
        target=batch/'review'/filename
        if not target.exists():save_csv(target,records,fieldnames)
    save(batch/'review/package.json',{'pool_version':digest(pool),'items':len(pool),'queries':len(d['queries']),'html_sha256':sha_file(path),'generated_at':now(),'rank_method_score_hidden':True,'status':'AWAITING_HUMAN_REVIEW'})
    print(path.resolve())


def resume(args):
    batch=Path(args.batch);d=batch_data(batch);pool=read(batch/'current-pool.json') if (batch/'current-pool.json').exists() else d['pool']
    input_hashes={};provided={}
    previous={}
    if (batch/'current-round.json').exists():
        prior=read(batch/'current-round.json')['round_id'];previous=read(batch/'rounds'/prior/'receipt.json')['input_hashes']
    for kind,path in [('reviews',args.reviews),('query_reviews',args.query_reviews),('adjudications',args.adjudications)]:
        if not path and kind in previous:
            path=batch/'inputs'/f'{kind}-{previous[kind]}.csv'
        if path:
            p=Path(path);h=sha_file(p);input_hashes[kind]=h;target=batch/'inputs'/f'{kind}-{h}.csv';target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists() and sha_file(target)!=h:raise ValueError('append-only input copy changed')
            if not target.exists():shutil.copyfile(p,target)
            provided[kind]=csv_rows(target)
    docs=d['documents'];resolved=resolve_reviews(pool,d['queries'],{k:issue_text(x) for k,x in docs.items()},{k:x['html_url'] for k,x in docs.items()},provided.get('reviews',[]),provided.get('query_reviews',[]),provided.get('adjudications',[]))
    runs=d['runs']
    if (batch/'new-runs.jsonl').exists():
        additions=rows(batch/'new-runs.jsonl');recorded=[]
        for receipt_path in sorted((batch/'experiments').glob('*/receipt.json')):
            experiment_receipt=read(receipt_path)
            if experiment_receipt['experiment'] not in {'K1','R1'}:continue
            rp=receipt_path.parent/'runs.jsonl'
            if sha_file(rp)!=experiment_receipt['runs_sha256']:raise ValueError('immutable candidate run bytes changed')
            recorded+=rows(rp)
        if sorted(additions,key=lambda r:r['run_id'])!=sorted(recorded,key=lambda r:r['run_id']):raise ValueError('candidate records differ from experiment receipts')
        for r in additions:
            q=d['queries'][r['query_id']];s=d['scopes'][(r['repository'],r['corpus_scope'])];allowed={f'{r["repository"]}#{x["number"]}' for x in s['issues']}
            if r['query_sha256']!=q['query_sha256'] or r['corpus_hash']!=s['version'] or r['selected_doc_ids_hash']!=s['ids_hash'] or r['model_revision']!=d['manifest']['config']['model_revision'] or r['config_hash']!=d['manifest']['config_hash'] or any(x['doc_id'] not in allowed for x in r['ranked_results']):raise ValueError('candidate query/document/scope/model identity mismatch')
        runs=runs+additions
    scope_ids={key:{f'{key[0]}#{x["number"]}' for x in s['issues']} for key,s in d['scopes'].items()}
    result=score_records(runs,d['queries'],d['cases'],pool,resolved,scope_ids)
    versions={name:sha_file(ROOT/name) for name in ['evaluation/scenario_followup.py','evaluation/followup_scoring.py','evaluation/followup_report.py','evaluation/followup_review.py']}
    round_id='round_'+digest([input_hashes,result['pool_version'],result['qrels_version'],versions])[:16];round_dir=batch/'rounds'/round_id
    receipt={'round_id':round_id,'input_hashes':input_hashes,'pool_version':result['pool_version'],'qrels_version':result['qrels_version'],
             'scorer_version':'scenario_followup_v2','scorer_code_hashes':{k:v for k,v in versions.items() if k!='evaluation/followup_report.py'},'reporter_code_hashes':{'evaluation/followup_report.py':versions['evaluation/followup_report.py']},
             'scoring_config_hash':sha_file(CONFIG),'review_schema_version':2,'parent_rankings_sha256':d['lineage']['parent_rankings_sha256']}
    if round_dir.exists():
        if read(round_dir/'receipt.json')!=receipt or read(round_dir/'score.json')!=result:raise ValueError('existing scoring round changed')
    else:
        save(round_dir/'receipt.json',receipt);save(round_dir/'score.json',result);save(round_dir/'qrels.json',resolved)
    save(batch/'current-round.json',{'round_id':round_id,'state':result['state']})
    from evaluation.followup_report import report
    report(batch)
    print(json.dumps({'round':round_id,'state':result['state'],'humans':result['human_reviewers'],'comparison_queries':result['comparison_queries']}))


def main():
    parser=argparse.ArgumentParser(description=__doc__);sub=parser.add_subparsers(dest='command',required=True)
    p=sub.add_parser('audit');p.add_argument('--parent-run',required=True);p.add_argument('--out',required=True)
    for name in ['prepare-review','diagnose','reproduce','resume','report','run-approved','verify-publication']:
        p=sub.add_parser(name);p.add_argument('--batch',required=True)
        if name=='resume':
            for option in ['reviews','query-reviews','adjudications']:p.add_argument('--'+option)
        if name=='run-approved':p.add_argument('--experiment',choices=['K1','R1','E1','E2','E3'],required=True);p.add_argument('--approval-file',required=True)
    args=parser.parse_args()
    if args.command=='audit':audit(args)
    elif args.command=='prepare-review':prepare_review(args)
    elif args.command=='resume':resume(args)
    elif args.command in {'diagnose','reproduce','run-approved'}:
        from evaluation.followup_retrieval import diagnose,reproduce,run_approved
        {'diagnose':diagnose,'reproduce':reproduce,'run-approved':run_approved}[args.command](args)
    else:
        from evaluation.followup_report import report,verify_publication
        {'report':report,'verify-publication':verify_publication}[args.command](Path(args.batch))


if __name__=='__main__':main()
