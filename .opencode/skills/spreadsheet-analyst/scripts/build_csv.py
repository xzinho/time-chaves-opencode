#!/usr/bin/env python3
import argparse,csv,json
from pathlib import Path
a=argparse.ArgumentParser();a.add_argument('--input',required=True);a.add_argument('--output',required=True);x=a.parse_args();d=json.loads(Path(x.input).read_text());rows=d.get('rows',[]);
if not rows or not isinstance(rows,list) or not isinstance(rows[0],dict): raise SystemExit('rows required')
with Path(x.output).open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
