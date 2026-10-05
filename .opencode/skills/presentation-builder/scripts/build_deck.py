#!/usr/bin/env python3
import argparse,html,json
from pathlib import Path
a=argparse.ArgumentParser();a.add_argument('--input',required=True);a.add_argument('--output',required=True);x=a.parse_args();d=json.loads(Path(x.input).read_text());slides=d.get('slides',[]);
if not slides: raise SystemExit('slides required')
s=''.join(f'<section><h1>{html.escape(str(v.get("title","")))}</h1><p>{html.escape(str(v.get("body","")))}</p></section>' for v in slides);Path(x.output).write_text('<style>section{width:1280px;height:720px;padding:80px;box-sizing:border-box;font:28px system-ui;border-bottom:1px solid #ccc}h1{font-size:64px}</style>'+s)
