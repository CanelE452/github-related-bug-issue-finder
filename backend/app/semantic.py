import json
import os
import threading
from pathlib import Path

import numpy as np

from .domain import ServiceError, issue_text
from .storage import digest


def chunk_text(text, tokenizer, size=448, overlap=64):
    ids = tokenizer.encode(text, add_special_tokens=False, verbose=False)
    if not ids:
        return ['']
    chunks = []
    for start in range(0, len(ids), size - overlap):
        chunks.append(tokenizer.decode(ids[start:start + size], skip_special_tokens=True))
        if start + size >= len(ids):
            break
    return chunks


class SemanticSearch:
    def __init__(self, settings):
        self.settings = settings
        self.directory = settings.data_dir / 'embeddings'
        self.directory.mkdir(parents=True, exist_ok=True)
        self.model = None
        self.revision = None
        self.lock = threading.RLock()
        self.corpora = {}

    def load_model(self):
        if self.model is not None:
            return
        try:
            from sentence_transformers import SentenceTransformer
            from huggingface_hub import HfApi
            import torch
            torch.set_num_threads(min(4, os.cpu_count() or 1))
            revision_file = self.directory / f'{digest(self.settings.model_name)}.revision.json'
            revision = self.settings.model_revision
            if not revision and revision_file.exists():
                revision = json.loads(revision_file.read_text())['revision']
            if not revision:
                revision = HfApi().model_info(self.settings.model_name).sha
            cached_model = self.settings.data_dir / 'models' / ('models--' + self.settings.model_name.replace('/', '--')) / 'snapshots' / revision
            complete_marker = cached_model / '.issue-finder-complete'
            if complete_marker.exists():
                self.model = SentenceTransformer(str(cached_model), device=self.settings.device,
                                                 local_files_only=True, trust_remote_code=False)
            else:
                self.model = SentenceTransformer(self.settings.model_name, revision=revision,
                                                 device=self.settings.device,
                                                 cache_folder=str(self.settings.data_dir / 'models'), trust_remote_code=False)
                if cached_model.exists():
                    complete_marker.touch()
            self.revision = revision
            revision_file.write_text(json.dumps({'revision': revision}), encoding='utf-8')
        except ImportError as exc:
            raise ServiceError('semantic_dependencies_missing',
                               '다국어 검색 의존성을 설치한 뒤 저장소를 다시 분석하세요. README의 semantic 설치 명령을 확인하세요.', 503) from exc
        except Exception as exc:
            self.model = None
            raise ServiceError('model_unavailable', '다국어 모델을 불러오지 못했습니다. 모델 다운로드 연결과 서버 설정을 확인하세요.', 503) from exc

    def settings_key(self):
        return {'model': self.settings.model_name, 'requested_revision': self.settings.model_revision,
                'chunk_size': self.settings.chunk_size, 'overlap': self.settings.chunk_overlap,
                'pooling': 'max_chunk_cosine', 'prefix_version': 1}

    def manifest_path(self, snapshot):
        return self.directory / f"{digest([snapshot['repository'], snapshot['version'], self.settings_key()])}.manifest.json"

    def ready(self, snapshot):
        return self.manifest_path(snapshot).exists()

    def encode(self, text, prefix):
        chunks = chunk_text(text, self.model.tokenizer, self.settings.chunk_size, self.settings.chunk_overlap)
        vectors = self.model.encode([prefix + x for x in chunks], normalize_embeddings=True,
                                    batch_size=32, show_progress_bar=False, convert_to_numpy=True)
        return np.asarray(vectors, dtype=np.float32)

    def prepare(self, snapshot, issues, progress=None):
        with self.lock:
            self.load_model()
            entries = []
            for index, issue in enumerate(issues):
                body_hash = digest(issue_text(issue))
                key = digest([body_hash, self.settings_key(), self.revision])
                file = self.directory / f'{key}.npy'
                valid_cache = False
                if file.exists():
                    try:
                        cached = np.load(file, allow_pickle=False)
                        valid_cache = cached.ndim == 2 and len(cached) > 0 and np.isfinite(cached).all()
                    except (ValueError, OSError):
                        pass
                if not valid_cache:
                    vectors = self.encode(issue_text(issue), 'passage: ')
                    temporary = file.with_suffix('.tmp')
                    with temporary.open('wb') as handle:
                        np.save(handle, vectors, allow_pickle=False)
                    os.replace(temporary, file)
                entries.append({'number': issue['number'], 'body_hash': body_hash, 'file': file.name})
                if progress:
                    progress({'embedded_count': index + 1, 'bug_issue_count': len(issues)})
            manifest = {'settings': self.settings_key(), 'resolved_revision': self.revision,
                        'snapshot_version': snapshot['version'], 'entries': entries}
            target = self.manifest_path(snapshot)
            temporary = target.with_suffix('.tmp')
            temporary.write_text(json.dumps(manifest), encoding='utf-8')
            os.replace(temporary, target)
            self.corpora.pop(str(target), None)

    def scores(self, snapshot, query):
        with self.lock:
            path = self.manifest_path(snapshot)
            if not path.exists():
                raise ServiceError('semantic_not_ready', '다국어 인덱스가 아직 준비되지 않았습니다. 다국어 검색 준비를 선택해 분석하세요.', 409)
            self.load_model()
            manifest = json.loads(path.read_text(encoding='utf-8'))
            if manifest['resolved_revision'] != self.revision:
                raise ServiceError('model_revision_changed', '모델 버전이 변경되었습니다. 인덱스를 다시 생성하세요.', 409)
            key = str(path)
            if key not in self.corpora:
                try:
                    self.corpora[key] = [(entry['number'], np.load(self.directory / entry['file'], allow_pickle=False))
                                         for entry in manifest['entries']]
                except (OSError, ValueError) as exc:
                    raise ServiceError('embedding_cache_invalid', '임베딩 캐시를 읽지 못했습니다. 인덱스를 다시 생성하세요.', 503) from exc
            query_vectors = self.encode(query, 'query: ')
            return {number: float(np.max(vectors @ query_vectors.T)) for number, vectors in self.corpora[key]}
