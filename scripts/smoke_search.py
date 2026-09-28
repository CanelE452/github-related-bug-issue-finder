"""Exercise real local API searches; examples are smoke checks, not labeled evaluation."""
import json
from pathlib import Path

import httpx


def main():
    cases = [
        ('en', 'Model loading fails because the GPU runs out of memory.', 'CUDA out of memory'),
        ('ko', '모델을 불러올 때 GPU 메모리가 부족해서 실행이 멈춰요.', ''),
        ('en', 'Text to audio pipeline fails because BatchEncoding.to does not accept dtype.', 'TypeError'),
        ('ko', '음성 생성 파이프라인에서 dtype 인자를 지원하지 않는다는 오류가 발생해요.', ''),
    ]
    results = []
    with httpx.Client(base_url='http://127.0.0.1:8000', timeout=180) as client:
        for language, problem, error in cases:
            for method in ['bm25', 'semantic', 'hybrid']:
                response = client.post('/api/search', json={'repository': 'huggingface/transformers', 'problem': problem,
                                                          'error': error, 'method': method})
                response.raise_for_status()
                data = response.json()
                assert len(data['results']) <= 5
                assert all('/huggingface/transformers/issues/' in x['url'] for x in data['results'])
                results.append({'language': language, 'problem': problem, **data})
                print(json.dumps({'language': language, 'method': method, 'count': len(data['results']),
                                  'top5': [x['number'] for x in data['results']], 'elapsed_ms': data['elapsed_ms']}), flush=True)
    output = Path('evaluation/output/smoke-search.json')
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps({'kind': 'unlabeled_functional_smoke_test', 'cases': results}, ensure_ascii=False, indent=2), encoding='utf-8')


if __name__ == '__main__':
    main()
