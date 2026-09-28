"""Reproducible retrieval evaluation against a frozen SQLite snapshot."""
import argparse
import csv
import json
import math
import random
import statistics
import time
from pathlib import Path

from backend.app.config import Settings
from backend.app.domain import is_bug, query_text, repository_name
from backend.app.search import SearchEngine
from backend.app.semantic import SemanticSearch
from backend.app.storage import Store, digest


def split_pairs(pairs, seed=42):
    # Connected components keep chains, shared canonical issues and translations together.
    parent = {}
    def root(x):
        parent.setdefault(x, x)
        if parent[x] != x:
            parent[x] = root(parent[x])
        return parent[x]
    for p in pairs:
        a, b = (p['repository'], p['query_number']), (p['repository'], p['target_number'])
        parent[root(a)] = root(b)
    groups = sorted({root((p['repository'], p['target_number'])) for p in pairs})
    random.Random(seed).shuffle(groups)
    validation = set(groups[:math.floor(len(groups) * .3)])
    return [{**p, 'split': 'validation' if root((p['repository'], p['target_number'])) in validation else 'test'} for p in pairs]


def rank_metrics(ranks):
    n = len(ranks)
    if not n:
        return {'count': 0, 'recall_at_1': None, 'recall_at_5': None, 'mrr': None}
    return {'count': n, 'recall_at_1': sum(r == 1 for r in ranks) / n,
            'recall_at_5': sum(r is not None and r <= 5 for r in ranks) / n,
            'mrr': sum(1 / r if r else 0 for r in ranks) / n}


def eligible_pairs(pairs, snapshot):
    records = {x['number']: x for x in snapshot['issues']}
    bugs = {n for n, x in records.items() if is_bug(x, snapshot['bug_labels'])}
    eligible, excluded = [], []
    seen = set()
    for p in pairs:
        if p['repository'] != snapshot['repository']:
            continue
        reason = None
        identity = (p['query_number'], p['target_number'], p.get('language', 'en'))
        if identity in seen:
            reason = 'duplicate_pair'
        seen.add(identity)
        if not p.get('source_url'):
            reason = 'missing_evidence'
        elif p['query_number'] == p['target_number']:
            reason = 'self_pair'
        elif p['target_number'] not in records:
            reason = 'target_outside_snapshot'
        elif p['target_number'] not in bugs:
            reason = 'target_excluded_by_bug_filter'
        elif p['query_number'] not in records:
            reason = 'query_outside_snapshot'
        elif p.get('language', 'en') == 'ko' and (not p.get('reviewed_by') or not p.get('query_text')):
            reason = 'korean_query_requires_human_review'
        if reason:
            excluded.append({**p, 'reason': reason})
            continue
        issue = records[p['query_number']]
        text = p.get('query_text') if p.get('language') == 'ko' else query_text(issue['title'], issue.get('body') or '')
        eligible.append({**p, 'query_text': text, 'language': p.get('language', 'en')})
    return eligible, excluded


def evaluate(engine, snapshot, pairs, methods, split='test'):
    eligible, excluded = eligible_pairs(pairs, snapshot)
    # Split all sourced pairs, including currently out-of-snapshot targets, for stable assignment.
    assignments = split_pairs(pairs)
    split_by_id = {(p['repository'], p['query_number'], p['target_number']): p['split'] for p in assignments}
    selected = [{**p, 'split': split_by_id[(p['repository'], p['query_number'], p['target_number'])]} for p in eligible]
    selected = [p for p in selected if p['split'] == split]
    rows = []
    for p in selected:
        for method in methods:
            started = time.perf_counter()
            ranked = engine.ranking(snapshot, p['query_text'], method, exclude=p['query_number'])
            elapsed = (time.perf_counter() - started) * 1000
            rank = next((i for i, (number, _) in enumerate(ranked, 1) if number == p['target_number']), None)
            rows.append({'query_number': p['query_number'], 'target_number': p['target_number'],
                         'language': p['language'], 'method': method, 'split': split, 'rank': rank,
                         'elapsed_ms': elapsed, 'top5': [n for n, _ in ranked[:5]], 'source_url': p['source_url']})
    summaries = []
    for language in sorted({p['language'] for p in selected}):
        for method in methods:
            group = [r for r in rows if r['language'] == language and r['method'] == method]
            summaries.append({'language': language, 'method': method, 'split': split,
                              **rank_metrics([r['rank'] for r in group]),
                              'mean_ms': statistics.mean(r['elapsed_ms'] for r in group) if group else None,
                              'exploratory': len(group) < 50})
    return {'repository': snapshot['repository'], 'snapshot_version': snapshot['version'],
            'pairs_hash': digest(pairs), 'bug_labels': snapshot['bug_labels'], 'partial': snapshot['partial'],
            'seed': 42, 'split': split, 'eligible_pairs': len(eligible), 'evaluated_pairs': len(selected),
            'excluded': excluded, 'summaries': summaries, 'queries': rows,
            'limitations': ['Duplicate retrieval is a proxy for relatedness, not a complete relevance judgment.',
                           'Snapshot evaluation uses current issue text, not reconstructed historical text.',
                           'Hybrid MRR is limited to the union of top-50 candidates from each retriever.',
                           'No claim of improvement with fewer than 50 evaluation pairs.',
                           'Korean queries require query_text and a human reviewed_by value; never machine-certified.']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repository', required=True)
    parser.add_argument('--pairs', default='evaluation/output/pairs.json')
    parser.add_argument('--methods', nargs='+', default=['bm25', 'semantic', 'hybrid'], choices=['bm25', 'semantic', 'hybrid'])
    parser.add_argument('--split', choices=['validation', 'test'], default='test')
    parser.add_argument('--output', default='evaluation/output/results')
    args = parser.parse_args()
    settings = Settings()
    store = Store(settings.data_dir)
    snapshot = store.get(repository_name(args.repository))
    if not snapshot:
        parser.error('먼저 survey 또는 API로 저장소를 수집하세요.')
    pairs = json.loads(Path(args.pairs).read_text(encoding='utf-8'))
    semantic = SemanticSearch(settings)
    engine = SearchEngine(store, semantic)
    issues, _, _ = engine.index(snapshot)
    if set(args.methods) & {'semantic', 'hybrid'}:
        semantic.prepare(snapshot, issues)
    report = evaluate(engine, snapshot, pairs, args.methods, args.split)
    report['model'] = {'name': settings.model_name, 'resolved_revision': semantic.revision,
                       'chunk_size': settings.chunk_size, 'chunk_overlap': settings.chunk_overlap}
    report['retrieval'] = {'rrf_constant': 60, 'rrf_window': 50, 'bm25': 'Okapi k1=1.5 b=0.75 positive Robertson IDF'}
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.with_suffix('.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    with output.with_suffix('.csv').open('w', newline='', encoding='utf-8-sig') as f:
        fields = ['language', 'method', 'split', 'count', 'recall_at_1', 'recall_at_5', 'mrr', 'mean_ms', 'exploratory']
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(report['summaries'])
    print(json.dumps({'eligible_pairs': report['eligible_pairs'], 'evaluated_pairs': report['evaluated_pairs'], 'excluded': len(report['excluded']), 'summaries': report['summaries']}, ensure_ascii=True, indent=2))


if __name__ == '__main__':
    main()
