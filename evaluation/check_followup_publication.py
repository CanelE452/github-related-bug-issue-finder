"""Test a Git-index archive, excluding unrelated working-tree changes."""
import argparse
import io
import os
import subprocess
import sys
import uuid
import zipfile
from pathlib import Path

from backend.app.config import ROOT
from evaluation.scenario_followup import save
from evaluation.scenario_eval import now,sha_file
from evaluation.followup_report import public_text,artifact_manifest


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--batch',required=True);args=p.parse_args();batch=Path(args.batch).resolve()
    # Archive exact repository blobs, independent of Windows checkout line endings.
    git=['git','-c','safe.directory='+ROOT.as_posix(),'-c','core.autocrlf=false']
    tree=subprocess.check_output(git+['write-tree'],cwd=ROOT,text=True).strip();archive=subprocess.check_output(git+['archive','--format=zip',tree],cwd=ROOT)
    source=batch/'publication-check'/tree;source.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(io.BytesIO(archive)) as z:
        for name in z.namelist():
            candidate=(source/name).resolve()
            if source.resolve() not in candidate.parents and candidate!=source.resolve():raise ValueError('archive path escapes publication workspace')
        z.extractall(source)
    code_hashes={f.relative_to(source).as_posix():sha_file(f) for f in sorted(source.rglob('*')) if f.is_file() and (f.suffix in {'.py','.ts','.tsx','.css','.js'} or f.name.startswith('requirements'))}
    # Keep paths below Windows MAX_PATH even with pytest's names and cache hashes.
    temporary=ROOT/'data'/('pt-'+uuid.uuid4().hex[:8])
    if temporary.exists() or ROOT.resolve() not in temporary.resolve().parents:raise ValueError('test temporary directory must be fresh and inside workspace')
    started=now();result=subprocess.run([sys.executable,'-m','pytest','backend/tests','-q','-p','no:cacheprovider','--basetemp',str(temporary)],cwd=source,capture_output=True,text=True,encoding='utf-8',env={**os.environ,'PYTHONIOENCODING':'utf-8'})
    original=result.stdout+result.stderr;local=batch/'publication-check'/f'{tree}.tests.txt';local.write_text(original,encoding='utf-8',newline='\n')
    output=ROOT/'docs/experiments/scenario_followup_v2'/batch.name;published=output/'tests/published-tree.txt';published.write_text(public_text(original),encoding='utf-8',newline='\n')
    save(output/'tests/published-tree.json',{'source_tree_id':tree,'code_and_test_byte_hashes':code_hashes,'command':'python -m pytest backend/tests -q -p no:cacheprovider --basetemp <fresh workspace test directory>','started_at':started,'finished_at':now(),'exit_code':result.returncode,'source_log_sha256':sha_file(local),'public_log_sha256':sha_file(published),'masked':original!=public_text(original),'note':'After adding this log, Git tree ID changes. Code/test byte hashes identify the tested code; final publication must match these hashes.'})
    artifact_manifest(output);print(public_text(original));print('PUBLICATION_SOURCE_TREE',tree,'EXIT_CODE',result.returncode)
    if result.returncode:raise SystemExit(result.returncode)


if __name__=='__main__':main()
