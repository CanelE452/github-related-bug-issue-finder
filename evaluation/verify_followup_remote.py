"""Fetch commit-fixed GitHub artifacts; credentials remain in memory, never logged."""
import argparse
import io
import subprocess
from pathlib import Path

import httpx
from PIL import Image

from backend.app.config import ROOT
from evaluation.scenario_eval import sha_file,now,read
from evaluation.scenario_followup import save


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--batch',required=True);parser.add_argument('--commit',required=True);args=parser.parse_args()
    if len(args.commit)!=40 or any(c not in '0123456789abcdef' for c in args.commit):raise ValueError('full commit SHA required')
    batch=Path(args.batch);output=ROOT/'docs/experiments/scenario_followup_v2'/batch.name;repo='CanelE452/github-related-bug-issue-finder'
    git=['git','-c','safe.directory='+ROOT.as_posix()];remote=subprocess.check_output(git+['remote','get-url','origin'],cwd=ROOT,text=True).strip()
    if remote not in {f'https://github.com/{repo}.git',f'https://github.com/{repo}'}:raise ValueError('unexpected repository destination')
    # Standard Git credential manager for this existing, user-authorized GitHub remote.
    credential=subprocess.run(git+['credential','fill'],cwd=ROOT,input='protocol=https\nhost=github.com\n\n',text=True,capture_output=True,check=True)
    values=dict(line.split('=',1) for line in credential.stdout.splitlines() if '=' in line)
    if not values.get('password'):raise ValueError('existing GitHub credential not available')
    paths=['README.md','report.md','status.json','lineage.json','casebook.md','casebook/O-E1.md','rankings/O-E1.jsonl','metrics_by_query.csv','metrics_summary.csv','review_progress.csv','figure_data/generation.json','artifact_manifest.json','tests/published-tree.json','tests/published-tree.txt']
    paths+=[p.relative_to(output).as_posix() for p in sorted((output/'images').glob('*.png'))]
    maximum=read(ROOT/'evaluation/scenario_followup_v2/config.json')['max_http_calls'];checked=[];calls=0;errors=[]
    ledger_path=batch/'http-verification-ledger.json';ledger=read(ledger_path) if ledger_path.exists() else []
    archive=batch/'remote-verification'/args.commit;archive.mkdir(parents=True,exist_ok=True)
    with httpx.Client(timeout=30,headers={'Authorization':'Bearer '+values['password'],'Accept':'application/vnd.github.raw+json','X-GitHub-Api-Version':'2022-11-28'},follow_redirects=False) as client:
        for path in paths:
            if len(ledger)>=maximum:raise ValueError('cumulative remote HTTP budget exhausted')
            relative='docs/experiments/scenario_followup_v2/'+batch.name+'/'+path;calls+=1
            ledger.append({'path':relative,'commit':args.commit,'attempted_at':now()});save(ledger_path,ledger)
            response=client.get(f'https://api.github.com/repos/{repo}/contents/{relative}',params={'ref':args.commit})
            if response.status_code!=200:
                errors.append({'path':path,'status':response.status_code});continue
            target=archive/path;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(response.content)
            if sha_file(target)!=sha_file(output/path):errors.append({'path':path,'status':'BYTE_HASH_MISMATCH'});continue
            if path.endswith('.png'):
                with Image.open(io.BytesIO(response.content)) as image:image.verify()
            checked.append({'path':path,'bytes':len(response.content),'sha256':sha_file(target),'commit_url':f'https://github.com/{repo}/blob/{args.commit}/{relative}'})
    receipt={'commit':args.commit,'branch':'main','checked_at':now(),'http_calls':calls,'cumulative_http_calls':len(ledger),'checked_files':checked,'errors':errors,'status':'VERIFIED' if not errors else 'REMOTE_VERIFICATION_FAILED','credential_logged':False}
    save(batch/'publication-receipt.json',receipt);print({'commit':args.commit,'http_calls':calls,'verified_files':len(checked),'errors':errors,'status':receipt['status']})
    if errors:raise SystemExit(1)


if __name__=='__main__':main()
