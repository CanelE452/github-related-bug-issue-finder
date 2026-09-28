"""Read-only GitHub survey. Only explicit maintainer duplicate references become pairs."""
import argparse
import json
import re
from collections import Counter
from pathlib import Path

from backend.app.config import Settings
from backend.app.domain import ServiceError, bug_labels, is_bug, repository_name
from backend.app.github import GitHubClient
from backend.app.storage import Store


def explicit_duplicate(comment, repository):
    if comment.get('author_association') not in {'OWNER', 'MEMBER', 'COLLABORATOR'}:
        return []
    # Accept GitHub's explicit "Duplicate of" convention; never infer a target from labels.
    pattern = r'(?im)^\s*(?:this (?:issue )?is (?:a )?)?duplicate of\s+(?:#(\d+)|https://github\.com/' + re.escape(repository) + r'/issues/(\d+))\b'
    return [int(a or b) for a, b in re.findall(pattern, comment.get('body') or '', re.IGNORECASE)]


def collect_pairs(client, repository, issues, max_candidates=8):
    candidates = [x for x in issues if x.get('state_reason') == 'duplicate' or
                  any('duplicate' in label['name'].lower() for label in x.get('labels', []))]
    pairs, errors = [], []
    for issue in candidates[:max_candidates]:
        try:
            events = []
            for page in range(1, 3):
                response = client.get(f"/repos/{repository}/issues/{issue['number']}/timeline", per_page=100, page=page)
                events.extend(response.json())
                if 'next' not in response.links:
                    break
            # A truncated timeline could hide a later unmark/retraction; do not assert a pair.
            if 'next' in response.links:
                continue
            marked = [e for e in events if e.get('event') in {'marked_as_duplicate', 'unmarked_as_duplicate'}]
            if marked and marked[-1]['event'] == 'unmarked_as_duplicate':
                continue
            comments = [e for e in events if e.get('event') == 'commented']
            targets = [(n, c) for c in comments for n in explicit_duplicate(c, repository)]
            distinct = {n for n, _ in targets if n != issue['number']}
            if len(distinct) == 1:
                target = next(iter(distinct))
                comment = next(c for n, c in targets if n == target)
                pairs.append({'repository': repository, 'query_number': issue['number'], 'target_number': target,
                              'source_url': comment['html_url'], 'evidence': 'explicit_maintainer_duplicate_comment',
                              'source_text': comment['body'], 'query_title': issue['title'], 'query_body': issue.get('body') or '',
                              'language': 'en'})
        except ServiceError as exc:
            errors.append({'query_number': issue['number'], **exc.as_dict()})
            if exc.code == 'github_rate_limit':
                break
    return pairs, errors, len(candidates)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repositories', nargs='+', default=['huggingface/transformers', 'pytorch/pytorch'])
    parser.add_argument('--pages', type=int, default=20, choices=range(1, 21))
    parser.add_argument('--max-candidates', type=int, default=8)
    parser.add_argument('--output', default='evaluation/output/survey.json')
    parser.add_argument('--reuse-cache', action='store_true')
    args = parser.parse_args()
    settings = Settings()
    store, client = Store(settings.data_dir), GitHubClient(settings.github_token)
    report = {'repositories': [], 'pairs': [], 'selection': None,
              'limitations': 'Recent capped snapshot; duplicate-label candidates with explicit maintainer comments only. Not exhaustive.'}
    try:
        for name in args.repositories:
            name = repository_name(name)
            try:
                snapshot = store.get(name) if args.reuse_cache else None
                if not snapshot:
                    snapshot = client.fetch(name, args.pages)
                labels = Counter(label['name'] for issue in snapshot['issues'] for label in issue.get('labels', []))
                # The actual observed label names are saved with the snapshot and reused by evaluation.
                selected = bug_labels([name for name in labels if re.search(r'(^|[\s:])bug($|[\s:])', name, re.I)])
                snapshot['bug_labels'] = selected
                snapshot['bug_issue_count'] = sum(is_bug(x, selected) for x in snapshot['issues'])
                snapshot = store.save(snapshot)
                pairs, errors, candidate_count = collect_pairs(client, name, snapshot['issues'], args.max_candidates)
                bug_numbers = {x['number'] for x in snapshot['issues'] if is_bug(x, selected)}
                valid = [p for p in pairs if p['target_number'] in bug_numbers]
                entry = {k: snapshot[k] for k in ['repository', 'fetched_count', 'issue_count', 'bug_issue_count', 'bug_labels', 'partial', 'collected_at', 'version']}
                entry.update(top_labels=labels.most_common(20), duplicate_candidates=candidate_count,
                             verified_pairs=len(pairs), eligible_pairs=len(valid), errors=errors)
                report['repositories'].append(entry)
                report['pairs'].extend(pairs)
                print(json.dumps({k: entry[k] for k in ['repository', 'issue_count', 'bug_issue_count', 'verified_pairs', 'eligible_pairs']}, ensure_ascii=True), flush=True)
            except ServiceError as exc:
                report['repositories'].append({'repository': name, 'error': exc.as_dict()})
        available = [x for x in report['repositories'] if 'eligible_pairs' in x]
        if available:
            report['selection'] = max(available, key=lambda x: (x['eligible_pairs'], x['bug_issue_count']))['repository']
        target = Path(args.output)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
        target.with_name('pairs.json').write_text(json.dumps(report['pairs'], ensure_ascii=False, indent=2), encoding='utf-8')
        print(f'Saved {target}; selected={report["selection"]}', flush=True)
    finally:
        client.close()


if __name__ == '__main__':
    main()
