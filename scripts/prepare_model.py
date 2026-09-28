"""Download the pinned model and smoke-test multilingual encoding (no user inputs sent)."""
import json

from backend.app.config import Settings
from backend.app.semantic import SemanticSearch

if __name__ == '__main__':
    semantic = SemanticSearch(Settings())
    semantic.load_model()
    vectors = semantic.encode('GPU 메모리가 부족합니다. CUDA out of memory.', 'query: ')
    print(json.dumps({'model': semantic.settings.model_name, 'revision': semantic.revision, 'shape': list(vectors.shape)}))
