"""Mechanical diagnostics and strictly gated, single-factor follow-up searches."""
import re
import shutil
import time
from pathlib import Path
from types import SimpleNamespace

import numpy as np

from backend.app.domain import issue_text, query_text
from backend.app.search import tokenize, lexical_ranking, build_lexical_index, fuse
from backend.app.storage import digest
from evaluation.scenario_eval import read, rows, runtime, sha_file, now
from evaluation.scenario_followup import CONFIG, batch_data, save, save_rows
from evaluation.followup_scoring import provenance, extend_pool


def lexical_text(text):return re.sub(r'(?m)^\[(?:PROBLEM|ERROR|ENVIRONMENT)\]\n','',text)


def k1_tokens(text):
    original=tokenize(lexical_text(text));result=list(original);seen=set(original)
    for token in original:
        if not re.search('[가-힣]',token) or not re.search('[a-z]',token):continue
        for part in re.findall(r'[a-z0-9_]+(?:[.:/\\+\-][a-z0-9_]+)*',token):
            if re.search('[a-z]',part) and part not in seen:result.append(part);seen.add(part)
    return result


def k1_ranking(issues,tokens,bm25,text):
    if bm25 is None:return []
    q=k1_tokens(text);overlap=set(q);scores=bm25.get_scores(q)
    return sorted([(x['number'],float(scores[i])) for i,x in enumerate(issues) if overlap.intersection(tokens[i])],key=lambda x:(-x[1],x[0]))


def contribution(lexical,semantic,constant=60,window=50):
    fused=fuse(lexical,semantic,constant,window);lr={n:i for i,(n,_) in enumerate(lexical,1)};sr={n:i for i,(n,_) in enumerate(semantic,1)};fr={n:i for i,(n,_) in enumerate(fused,1)}
    result={}
    for n in set(lr)|set(sr):
        l,s=lr.get(n),sr.get(n);lt=1/(constant+l) if l and l<=window else 0.;st=1/(constant+s) if s and s<=window else 0.
        result[n]={'bm25_rank':l,'semantic_rank':s,'in_lexical_window':bool(l and l<=window),'in_semantic_window':bool(s and s<=window),
                   'lexical_rrf_term':lt,'semantic_rrf_term':st,'fused_score':lt+st,'fused_rank':fr.get(n)}
    return result


def diagnose(args):
    batch=Path(args.batch);d=batch_data(batch);scope=[];tokens=[];chunks=[]
    for c in d['cases'].values():
        for did in c['source_doc_ids']:
            scope.append({'case_id':c['case_id'],'cohort':c['cohort'],'doc_id':did,'url':c['source_urls'][0],
                          'in_C_raw':did in d['documents'],'in_C_bug':did in {f'{c["repository"]}#{x["number"]}' for x in d['scopes'][(c['repository'],'C_bug')]['issues']},
                          'source_sha256':c['source_hash'],'quality_status':'UNJUDGED'})
    for q in d['queries'].values():
        c=d['cases'][q['case_id']];repo=c['repository'];original=tokenize(lexical_text(q['query_text']));added=[x for x in k1_tokens(q['query_text']) if x not in original]
        for scope_name in ['C_raw','C_bug']:
            vocabulary={t for doc in d['scopes'][(repo,scope_name)]['issues'] for t in tokenize(issue_text(doc))}
            matches=sorted(set(original)&vocabulary)
            tokens.append({'query_id':q['query_id'],'repository':repo,'scope':scope_name,'query_text':q['query_text'],
                           'current_tokens':original,'matches':matches,'unmatched':sorted(set(original)-vocabulary),
                           'ascii_boundary_candidates':added,'candidates_in_corpus':sorted(set(added)&vocabulary),
                           'candidates_in_reference':sorted(set(added)&{t for did in c['source_doc_ids'] if did in d['documents'] for t in tokenize(issue_text(d['documents'][did]))}),
                           'bm25_empty':not matches,'quality_status':'UNJUDGED','diagnosis':'mechanical_token_output_only'})
    for r in d['runs']:
        for x in r.get('chunk_diagnostics',[]):chunks.append({'run_id':r['run_id'],'query_id':r['query_id'],'method':r['method'],'scope':r['corpus_scope'],**x,'evidence_id':'chunk_'+digest([r['run_id'],x['doc_id'],x['document_chunk'],x['query_chunk']])[:16]})
    save(batch/'diagnostics.json',{'created_at':now(),'scope':scope,'tokens':tokens,'chunk_records':len(chunks),'relevance_inferred':False})
    save_rows(batch/'chunk-evidence.local.jsonl',chunks)
    print({'scope_records':len(scope),'token_records':len(tokens),'chunk_records':len(chunks),'status':'MECHANICAL_ONLY'})


class Budget:
    def __init__(self,batch):
        self.batch=Path(batch);self.config=read(CONFIG);self.path=self.batch/'budget.json'
        self.value=read(self.path) if self.path.exists() else {'logical_conditions':0,'phase_counts':{},'compute_seconds':0.,'query_encode_calls':0,'document_reembedding_calls':0,'cache_hit_documents':0,'http_calls':0,'training_calls':0,'paid_api_calls':0}
    def reserve(self,phase,count,operation_id=None):
        reservations=self.value.setdefault('reservations',{})
        if operation_id in reservations:
            if reservations[operation_id]!={'phase':phase,'count':count}:raise ValueError('reservation identity changed')
            return
        if self.value['logical_conditions']+count>self.config['max_logical_conditions'] or self.value['phase_counts'].get(phase,0)+count>self.config['limits'][phase] or self.value['compute_seconds']>=self.config['max_compute_seconds']:raise ValueError('follow-up execution budget exhausted')
        self.value['logical_conditions']+=count;self.value['phase_counts'][phase]=self.value['phase_counts'].get(phase,0)+count
        if operation_id:reservations[operation_id]={'phase':phase,'count':count}
        save(self.path,self.value)
    def record(self,elapsed,encodes,hits):
        self.value['compute_seconds']+=elapsed;self.value['query_encode_calls']+=encodes;self.value['cache_hit_documents']+=hits;save(self.path,self.value)
    def checkpoint(self,started):
        if self.value['compute_seconds']+time.perf_counter()-started>=self.config['max_compute_seconds']:raise ValueError('compute budget reached; completed full-rank checkpoints preserved')


class FrozenRanks:
    def __init__(self,batch,data,budget):
        self.batch=Path(batch);self.data=data;self.budget=budget;self.semantic=None;self.indices={};self.query_vectors={}
    def initialize_semantic(self):
        if self.semantic:return
        parent=self.data['parent'];destination=self.batch/'index/embeddings';destination.mkdir(parents=True,exist_ok=True)
        for file in (parent/'index/embeddings').iterdir():
            if file.suffix not in {'.json','.npy'}:continue
            target=destination/file.name
            if not target.exists():shutil.copyfile(file,target)
            if sha_file(file)!=sha_file(target):raise ValueError('copied embedding cache byte hash mismatch')
        self.semantic=runtime(self.batch,self.data['manifest']);self.semantic.load_model()
    def full(self,q,repo,scope,phase='full_rank'):
        path=self.batch/'full-ranks'/f'{digest([q["query_sha256"],repo,scope])}.json'
        snapshot=self.data['scopes'][(repo,scope)]
        identity={'query_id':q['query_id'],'query_sha256':q['query_sha256'],'repository':repo,'scope':scope,'corpus_hash':snapshot['version'],'ids_hash':snapshot['ids_hash'],'model_revision':self.data['manifest']['config']['model_revision']}
        if path.exists():
            stored=read(path)
            if stored['identity']!=identity:raise ValueError('full-rank checkpoint identity mismatch')
            if stored['payload_hash']!=digest([stored['lexical'],stored['semantic']]):raise ValueError('full-rank checkpoint content mismatch')
            return stored['lexical'],stored['semantic']
        started=time.perf_counter();before=self.semantic.encode_calls if self.semantic else 0;self.budget.checkpoint(started)
        if (repo,scope) not in self.indices:self.indices[(repo,scope)]=build_lexical_index(snapshot['issues'])
        tokens,bm25=self.indices[(repo,scope)];lexical=lexical_ranking(snapshot['issues'],tokens,bm25,q['query_text'])
        self.initialize_semantic();sem=self.semantic;manifest=read(sem.manifest_path(snapshot))
        expected=[(x['number'],digest(issue_text(x))) for x in snapshot['issues']]
        if manifest['snapshot_version']!=snapshot['version'] or manifest['resolved_revision']!=sem.revision or manifest['settings']!=sem.settings_key() or [(e['number'],e['body_hash']) for e in manifest['entries']]!=expected:raise ValueError('actual embedding index membership/config mismatch')
        if q['query_sha256'] not in self.query_vectors:self.query_vectors[q['query_sha256']]=sem.encode(q['query_text'],'query: ')
        vectors=self.query_vectors[q['query_sha256']];ranking=[]
        for entry in manifest['entries']:
            self.budget.checkpoint(started);v=np.load(sem.directory/entry['file'],allow_pickle=False)
            if v.ndim!=2 or not np.isfinite(v).all():raise ValueError('invalid frozen document vectors')
            ranking.append((entry['number'],float(np.max(v@vectors.T))))
        ranking.sort(key=lambda x:(-x[1],x[0]));self.budget.record(time.perf_counter()-started,sem.encode_calls-before,len(ranking))
        save(path,{'identity':identity,'lexical':lexical,'semantic':ranking,'payload_hash':digest([lexical,ranking]),'created_at':now(),'parent_embedding_files_verified':True,'phase':phase})
        return lexical,ranking


def reproduce(args):
    batch=Path(args.batch);d=batch_data(batch)
    if (batch/'reproduction.json').exists():
        print({'reused':True,'status':read(batch/'reproduction.json')['status']});return
    if not all(d['lineage']['retrieval_code_matches'].values()):raise ValueError('parent retrieval code mismatch')
    chosen=[];seen=set()
    for c in d['cases'].values():
        if c['cohort']=='core_development' and c['repository'] not in seen:
            q=next(q for q in d['queries'].values() if q['case_id']==c['case_id'] and q['variant']=='A_ko_symptom');chosen.append(q);seen.add(c['repository'])
    count=len(chosen)*6;budget=Budget(batch);budget.reserve('reproduce',count,'baseline_reproduction');ranker=FrozenRanks(batch,d,budget);tests=[];contrib=[]
    tolerance=read(CONFIG)['score_absolute_tolerance'];save(batch/'reproduction-selection.json',{'query_ids':[q['query_id'] for q in chosen],'absolute_score_tolerance':tolerance,'reason':read(CONFIG)['query_selection'],'frozen_before_execution':now()})
    for q in chosen:
        repo=d['cases'][q['case_id']]['repository']
        for scope in ['C_raw','C_bug']:
            lexical,semantic=ranker.full(q,repo,scope,'reproduce');hybrid=fuse(lexical,semantic)
            for method,ranking in [('bm25',lexical),('semantic',semantic),('hybrid',hybrid)]:
                original=next(r for r in d['runs'] if r['kind']=='core' and r['query_id']==q['query_id'] and r['corpus_scope']==scope and r['method']==method)
                actual=[{'rank':i,'doc_id':f'{repo}#{n}','score':s} for i,(n,s) in enumerate(ranking[:20],1)]
                same_order=[x['doc_id'] for x in actual]==[x['doc_id'] for x in original['ranked_results']]
                delta=max((abs(a['score']-b['score']) for a,b in zip(actual,original['ranked_results'])),default=0.)
                tests.append({'query_id':q['query_id'],'scope':scope,'method':method,'rank_order_equal':same_order,'max_score_absolute_delta':delta,'passed':same_order and delta<=tolerance,'actual_top20':actual})
            all_contrib=contribution(lexical,semantic);numbers={n for n,_ in lexical[:5]+semantic[:5]+hybrid[:5]}|{d['cases'][q['case_id']]['reference_number']}
            for n in sorted(numbers):contrib.append({'query_id':q['query_id'],'scope':scope,'doc_id':f'{repo}#{n}',**all_contrib.get(n,{}),'quality_status':'UNJUDGED'})
    save(batch/'reproduction.json',{'status':'REPRODUCED' if all(x['passed'] for x in tests) else 'BLOCKED_REPRODUCTION_MISMATCH','conditions':len(tests),'checks':tests,'created_at':now(),'tolerance':tolerance,'query_encode_calls':budget.value['query_encode_calls'],'document_reembedding_calls':budget.value['document_reembedding_calls']})
    save(batch/'rrf-contributions.json',contrib);print({'conditions':len(tests),'passed':sum(x['passed'] for x in tests),'encodes':budget.value['query_encode_calls']})


def failure_gate(experiment,request,data,resolved,reproduction):
    if experiment not in {'K1','R1'}:raise ValueError('not a single-factor failure experiment')
    if reproduction.get('status')!='REPRODUCED':raise ValueError('baseline reproduction gate not met')
    provenance(request)
    qid=request.get('query_id');did=request.get('direct_doc_id');competitor=request.get('competitor_doc_id');scope=request.get('scope')
    if qid not in data['queries'] or request.get('query_sha256')!=data['queries'][qid]['query_sha256'] or scope not in {'C_raw','C_bug'} or not resolved['approval'][qid]['approved']:raise ValueError('failure query needs actual approval/hash/scope')
    judgments={r['doc_id']:r for r in resolved['qrels'] if r['query_id']==qid}
    if judgments.get(did,{}).get('grade')!=2 or competitor not in judgments or judgments[competitor]['grade'] is None:raise ValueError('direct and competing document human evidence required')
    baseline=next(r for r in data['runs'] if r['query_id']==qid and r['kind']=='core' and r['corpus_scope']==scope and r['method']==('bm25' if experiment=='K1' else 'hybrid'))
    top=[x['doc_id'] for x in baseline['ranked_results'][:5]]
    if did in top or competitor not in top or judgments[competitor]['grade']==2:raise ValueError('no validated Top-5 failure with less relevant competitor')
    q=data['queries'][qid];repo=baseline['repository'];snapshot=data['scopes'][(repo,scope)]
    if did not in {f'{repo}#{x["number"]}' for x in snapshot['issues']}:raise ValueError('scope exclusion is not a token/RRF failure')
    if experiment=='K1':
        original=tokenize(lexical_text(q['query_text']));added=set(k1_tokens(q['query_text']))-set(original)
        if not added.intersection(tokenize(issue_text(data['documents'][did]))):raise ValueError('missing technical token not reproduced in direct document')
    return {'gate_reason':request['reason'],'query_id':qid,'evidence_ids':[judgments[did]['review_item_id'],judgments[competitor]['review_item_id']],'experiment':experiment}


def behavior_gate(experiment,request,data,resolved):
    provenance(request);queries=request.get('queries',[])
    limits={'E1':8,'E2':4,'E3':2}
    if experiment not in limits or not queries or len(queries)>limits[experiment]:raise ValueError('invalid behavior query count')
    drafts={q['query_id']:q for q in read(Path(__file__).parent/'scenario_pilot_v1/E1-variants.draft.json')}
    seen=set();repo_counts={}
    for q in queries:
        provenance(q);qid=q['query_id'];repo=q['repository'];repo_counts[repo]=repo_counts.get(repo,0)+1
        if qid in seen or repo not in data['snapshots'] or qid in data['queries']:raise ValueError('new behavior query identity/repository invalid')
        seen.add(qid)
        if q['query_text']!=query_text(q['problem'],q.get('error',''),q.get('environment','')) or digest(q['query_text'])!=q['query_sha256']:raise ValueError('behavior query hash/input mismatch')
        if q.get('approved')!='yes':raise ValueError('actual behavior query approval required')
        if experiment=='E1':
            draft=drafts.get(qid)
            if not draft or any(q.get(k)!=draft.get(k) for k in ['base_query_id','case_id','query_sha256','query_text']) or q.get('equivalent_to_base')!='yes' or not resolved['approval'][q['base_query_id']]['approved']:raise ValueError('E1 requires approved frozen draft/base/equivalence')
        if experiment=='E2':
            evidence=q.get('condition_evidence',[])
            if not evidence or not q.get('pair_id') or not q.get('condition'):raise ValueError('E2 requires actual paired condition evidence')
            for e in evidence:
                provenance(e);doc=data['documents'].get(e['doc_id'])
                if not doc or e['document_sha256']!=digest(issue_text(doc)) or e.get('evidence_scope')!='title_body' or not e.get('evidence_quote') or ' '.join(e['evidence_quote'].split()) not in ' '.join(issue_text(doc).split()) or e.get('evidence_url')!=doc['html_url'] or not e['doc_id'].startswith(repo+'#'):raise ValueError('invalid E2 frozen condition evidence')
        if experiment=='E3':
            docs=q.get('control_documents',[])
            if not docs or len(docs)>20 or len({e['doc_id'] for e in docs})!=len(docs):raise ValueError('E3 finite control membership invalid')
            for e in docs:
                provenance(e);doc=data['documents'].get(e['doc_id'])
                if not doc or not e['doc_id'].startswith(repo+'#') or e['document_sha256']!=digest(issue_text(doc)) or e.get('grade') not in (0,1,2) or e.get('evidence_scope')!='title_body' or not e.get('evidence_quote') or ' '.join(e['evidence_quote'].split()) not in ' '.join(issue_text(doc).split()) or e.get('evidence_url')!=doc['html_url']:raise ValueError('E3 requires complete actual title/body judgments')
            if not any(e['grade']==2 for e in docs) or not any(e['grade']<2 for e in docs):raise ValueError('E3 needs a positive plus and nonempty certified minus')
    if experiment=='E2':
        if any(n!=2 for n in repo_counts.values()):raise ValueError('E2 exactly one pair per supplied repository')
        for repo in repo_counts:
            pair=[q for q in queries if q['repository']==repo]
            if pair[0]['pair_id']!=pair[1]['pair_id'] or pair[0]['condition']==pair[1]['condition'] or pair[0]['query_sha256']==pair[1]['query_sha256']:raise ValueError('E2 contrast pair needs two different actual query conditions')
    if experiment=='E3' and any(n>1 for n in repo_counts.values()):raise ValueError('E3 one control per repository')
    return queries


def run_approved(args):
    batch=Path(args.batch);data=batch_data(batch);round_id=read(batch/'current-round.json')['round_id'];resolved=read(batch/'rounds'/round_id/'qrels.json')
    request=read(args.approval_file);experiment=args.experiment;reproduction=read(batch/'reproduction.json')
    if reproduction['status']!='REPRODUCED':raise ValueError('baseline reproduction required before new search comparisons')
    if experiment in {'K1','R1'}:
        gate=failure_gate(experiment,request,data,resolved,reproduction)
        queries=[q for q in data['queries'].values() if data['cases'][q['case_id']]['cohort']=='core_development']
    else:queries=[{**q,'variant':q.get('variant',experiment)} for q in behavior_gate(experiment,request,data,resolved)];gate={'gate_reason':request['reason'],'experiment':experiment,'query_ids':[q['query_id'] for q in queries]}
    request_hash=sha_file(args.approval_file);out=batch/'experiments'/f'{experiment}-{request_hash[:16]}'
    if (out/'receipt.json').exists():
        receipt=read(out/'receipt.json')
        if receipt['request_hash']!=request_hash:raise ValueError('immutable experiment identity mismatch')
        print({'reused':True,'experiment':experiment});return
    if experiment in {'K1','R1'} and (batch/'new-runs.jsonl').exists() and any(r['protocol_experiment']==experiment for r in rows(batch/'new-runs.jsonl')):raise ValueError('one frozen run per experiment; create a separate batch for another request')
    budget=Budget(batch);ranker=FrozenRanks(batch,data,budget)
    if experiment=='R1':
        q=data['queries'][request['query_id']];repo=data['cases'][q['case_id']]['repository'];scope=request['scope']
        path=batch/'full-ranks'/f'{digest([q["query_sha256"],repo,scope])}.json'
        if not path.exists():budget.reserve('full_rank',1,'full:'+digest([q['query_sha256'],repo,scope]))
        lex,sem=ranker.full(q,repo,scope);n=int(request['direct_doc_id'].rsplit('#',1)[1]);row=contribution(lex,sem).get(n,{})
        if not (((row.get('bm25_rank') or 0)>50 and row.get('semantic_rank') in range(1,51)) or ((row.get('semantic_rank') or 0)>50 and row.get('bm25_rank') in range(1,51))):raise ValueError('R1 gate: actual cutoff contribution loss not reproduced')
        gate['cutoff_trace']=row
    factor=4 if experiment=='K1' else 2 if experiment=='R1' else 6;count=len(queries)*factor
    budget.reserve(experiment,count,experiment+':'+request_hash);out.mkdir(parents=True,exist_ok=True)
    approval_copy=out/'approval.original.json'
    if approval_copy.exists() and sha_file(approval_copy)!=request_hash:raise ValueError('approval checkpoint changed')
    if not approval_copy.exists():shutil.copyfile(args.approval_file,approval_copy)
    save(out/'gate.json',gate)
    result=rows(out/'runs.partial.jsonl') if (out/'runs.partial.jsonl').exists() else []
    completed_ids={r['run_id'] for r in result}
    for q in queries:
        repo=data['cases'][q['case_id']]['repository'] if experiment in {'K1','R1'} else q['repository']
        for scope in ['C_raw','C_bug'] if experiment!='E3' else ['control_plus','control_minus']:
            if experiment=='E3':
                membership=[e['doc_id'] for e in q['control_documents'] if scope=='control_plus' or e['grade']<2];docs=[data['documents'][did] for did in membership]
                snapshot={'repository':repo,'scope':scope,'issues':docs,'version':digest([q['query_sha256'],scope,membership]),'ids_hash':digest(membership),'bug_labels':data['manifest']['config']['bug_labels']}
                data['scopes'][(repo,scope)]=snapshot
                ranker.initialize_semantic();sem=ranker.semantic;original=read(sem.manifest_path(data['scopes'][(repo,'C_raw')]))
                save(sem.manifest_path(snapshot),{**original,'snapshot_version':snapshot['version'],'entries':[e for e in original['entries'] if f'{repo}#{e["number"]}' in membership]})
            # Full-rank logical extraction is charged separately (at most 72 conditions).
            rank_path=batch/'full-ranks'/f'{digest([q["query_sha256"],repo,scope])}.json'
            if experiment in {'K1','R1'} and not rank_path.exists():budget.reserve('full_rank',1,'full:'+digest([q['query_sha256'],repo,scope]))
            lexical,semantic=ranker.full(q,repo,scope,experiment)
            methods=['K1_bm25','K1_hybrid'] if experiment=='K1' else ['R1_hybrid'] if experiment=='R1' else ['bm25','semantic','hybrid']
            for method in methods:
                run_id=f'{q["query_id"]}|{scope}|{method}|{experiment}'
                if run_id in completed_ids:continue
                started=time.perf_counter()
                if method.startswith('K1'):
                    snapshot=data['scopes'][(repo,scope)];tokens,bm25=ranker.indices.get((repo,scope)) or build_lexical_index(snapshot['issues']);changed=k1_ranking(snapshot['issues'],tokens,bm25,q['query_text']);ranking=changed if method=='K1_bm25' else fuse(changed,semantic)
                elif method=='R1_hybrid':ranking=fuse(lexical,semantic,window=max(len(lexical),len(semantic)))
                else:ranking=lexical if method=='bm25' else semantic if method=='semantic' else fuse(lexical,semantic)
                budget.record(time.perf_counter()-started,0,0)
                result.append({'run_id':f'{q["query_id"]}|{scope}|{method}|{experiment}','query_id':q['query_id'],'query_sha256':q['query_sha256'],'case_id':q['case_id'],'repository':repo,'corpus_scope':scope,'method':method,
                               'kind':'core' if experiment in {'K1','R1'} else experiment,'protocol_experiment':experiment,'corpus_hash':data['scopes'][(repo,scope)]['version'],'selected_doc_ids_hash':data['scopes'][(repo,scope)]['ids_hash'],
                               'model_revision':data['manifest']['config']['model_revision'],'config_hash':data['manifest']['config_hash'],'candidate_code_sha256':sha_file(Path(__file__)),
                               'status':'ok' if ranking else 'no_lexical_match','ranked_results':[{'rank':i,'doc_id':f'{repo}#{n}','score':s,'score_type':'rrf' if 'hybrid' in method else 'cosine_similarity' if method=='semantic' else 'bm25'} for i,(n,s) in enumerate(ranking[:20],1)],'elapsed_ranking_only_ms':(time.perf_counter()-started)*1000})
                save_rows(out/'runs.partial.jsonl',result)
    save_rows(out/'runs.jsonl',result);save_rows(out/'queries.jsonl',queries)
    current=rows(batch/'new-runs.jsonl') if (batch/'new-runs.jsonl').exists() else []
    if experiment in {'K1','R1'}:
        if any(r['protocol_experiment']==experiment for r in current):raise ValueError('one frozen setting/run per experiment; create another batch for a new request')
        current+=result;save_rows(batch/'new-runs.jsonl',current)
        pool=read(batch/'current-pool.json') if (batch/'current-pool.json').exists() else data['pool'];pool=extend_pool(pool,current,data['queries'],{k:digest(issue_text(v)) for k,v in data['documents'].items()});save(batch/'current-pool.json',pool)
    else:
        pool=extend_pool([],result,{q['query_id']:q for q in queries},{k:digest(issue_text(v)) for k,v in data['documents'].items()});save(out/'review-pool.json',pool)
        cases={q['case_id']:data['cases'].get(q['case_id'],{'case_id':q['case_id'],'repository':q['repository'],'cohort':experiment}) for q in queries}
        from evaluation.followup_review import package
        package(out/'review',{q['query_id']:q for q in queries},cases,pool,data['documents'],read(CONFIG)['seed'])
    save(out/'receipt.json',{'experiment':experiment,'request_hash':request_hash,'conditions':len(result),'created_at':now(),'status':'ADDITIONAL_REVIEW_REQUIRED','quality_verified':False,'query_specific_judgments_not_transferred':True,'candidate_code_sha256':sha_file(Path(__file__)),'parent_retrieval_code_hashes':data['manifest']['code_hashes'],'runs_sha256':sha_file(out/'runs.jsonl')})
    print({'experiment':experiment,'conditions':len(result),'status':'ADDITIONAL_REVIEW_REQUIRED'})
