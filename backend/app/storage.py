import hashlib
import json
import sqlite3
from contextlib import contextmanager
from pathlib import Path


def digest(value) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


class Store:
    def __init__(self, directory: Path):
        directory.mkdir(parents=True, exist_ok=True)
        self.path = directory / 'issues.sqlite3'
        with self.connect() as db:
            db.executescript('''
                PRAGMA journal_mode=WAL;
                CREATE TABLE IF NOT EXISTS snapshots (
                    repository TEXT PRIMARY KEY, version TEXT NOT NULL,
                    metadata TEXT NOT NULL, issues TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS jobs (id TEXT PRIMARY KEY, payload TEXT NOT NULL);
            ''')

    @contextmanager
    def connect(self):
        db = sqlite3.connect(self.path, timeout=30)
        try:
            with db:
                yield db
        finally:
            db.close()

    def get(self, repository):
        with self.connect() as db:
            row = db.execute('SELECT metadata, issues, version FROM snapshots WHERE repository=?', (repository,)).fetchone()
        return {**json.loads(row[0]), 'issues': json.loads(row[1]), 'version': row[2]} if row else None

    def save(self, snapshot):
        issues = snapshot['issues']
        metadata = {k: v for k, v in snapshot.items() if k not in {'issues', 'version'}}
        version = digest({'issues': issues, 'bug_labels': metadata['bug_labels']})
        with self.connect() as db:
            db.execute('INSERT OR REPLACE INTO snapshots VALUES (?,?,?,?)',
                       (snapshot['repository'], version, json.dumps(metadata), json.dumps(issues)))
        return {**metadata, 'issues': issues, 'version': version}

    def job(self, job_id):
        with self.connect() as db:
            row = db.execute('SELECT payload FROM jobs WHERE id=?', (job_id,)).fetchone()
        return json.loads(row[0]) if row else None

    def save_job(self, job):
        with self.connect() as db:
            db.execute('INSERT OR REPLACE INTO jobs VALUES (?,?)', (job['id'], json.dumps(job)))

    def interrupt_jobs(self):
        with self.connect() as db:
            rows = db.execute('SELECT id, payload FROM jobs').fetchall()
            for job_id, payload in rows:
                job = json.loads(payload)
                if job['status'] not in {'completed', 'failed'}:
                    job.update(status='failed', error={'code': 'interrupted', 'message': '서버가 재시작되었습니다. 분석을 다시 실행하세요.'})
                    db.execute('UPDATE jobs SET payload=? WHERE id=?', (json.dumps(job), job_id))
