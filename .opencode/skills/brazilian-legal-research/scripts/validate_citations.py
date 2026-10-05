#!/usr/bin/env python3
import argparse,json,re
from pathlib import Path
a=argparse.ArgumentParser();a.add_argument('--input',required=True);a.add_argument('--output',required=True);x=a.parse_args();d=json.loads(Path(x.input).read_text());out=[]
for c in d.get('citations',[]):
 miss=[k for k in ['title','url','authority','date','jurisdiction'] if not c.get(k)];url=bool(re.match(r'https://',str(c.get('url',''))));out.append({'title':c.get('title'),'valid':not miss and url,'missing':miss+([] if url else ['https_url'])})
Path(x.output).write_text(json.dumps({'citations':out,'all_valid':bool(out) and all(v['valid'] for v in out)},indent=2))
