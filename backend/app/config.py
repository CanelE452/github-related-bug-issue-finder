import os
from dataclasses import dataclass, field
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[2]
load_dotenv(ROOT / '.env')


@dataclass
class Settings:
    data_dir: Path = field(default_factory=lambda: Path(os.getenv('ISSUE_FINDER_DATA_DIR', str(ROOT / 'data'))))
    github_token: str = field(default_factory=lambda: os.getenv('GITHUB_TOKEN', ''))
    model_name: str = field(default_factory=lambda: os.getenv('ISSUE_FINDER_MODEL', 'intfloat/multilingual-e5-small'))
    model_revision: str = field(default_factory=lambda: os.getenv('ISSUE_FINDER_MODEL_REVISION', ''))
    device: str = field(default_factory=lambda: os.getenv('ISSUE_FINDER_DEVICE', 'cpu'))
    max_pages: int = 20
    chunk_size: int = 448
    chunk_overlap: int = 64
