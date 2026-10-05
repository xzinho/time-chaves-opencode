#!/usr/bin/env python3
import argparse,json,re
from pathlib import Path
a=argparse.ArgumentParser();a.add_argument('--input',required=True);a.add_argument('--output',required=True);x=a.parse_args();d=json.loads(Path(x.input).read_text());edges=d.get('edges',[]);
if not edges: raise SystemExit('edges required')
clean=lambda s:re.sub(r'[^A-Za-z0-9_ -]','',str(s));lines=['flowchart LR']+[f'  {clean(a)} -->|{clean(label)}| {clean(b)}' for a,b,label in edges];Path(x.output).write_text('\n'.join(lines)+'\n')
