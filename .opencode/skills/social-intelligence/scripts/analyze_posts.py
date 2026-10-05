#!/usr/bin/env python3
import argparse,collections,json
from pathlib import Path
a=argparse.ArgumentParser();a.add_argument('--input',required=True);a.add_argument('--output',required=True);x=a.parse_args();d=json.loads(Path(x.input).read_text());posts=d.get('posts',[]);
if not posts: raise SystemExit('posts required')
formats=collections.Counter(str(p.get('format','unknown')) for p in posts);hooks=collections.Counter(str(p.get('hook','unknown')) for p in posts);Path(x.output).write_text(json.dumps({'sample_size':len(posts),'formats':formats,'hooks':hooks,'limitations':'Resultados dependem da amostra; não alegar tração sem métricas.'},indent=2,default=dict))
