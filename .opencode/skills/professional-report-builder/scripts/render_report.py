#!/usr/bin/env python3
import argparse,html,json
from pathlib import Path
a=argparse.ArgumentParser();a.add_argument('--input',required=True);a.add_argument('--output',required=True);x=a.parse_args();d=json.loads(Path(x.input).read_text());
req=['title','summary','recommendations'];miss=[k for k in req if not d.get(k)];
if miss: raise SystemExit('missing:'+','.join(miss))
items=''.join('<li>'+html.escape(str(v))+'</li>' for v in d['recommendations']);src=''.join('<li>'+html.escape(str(v))+'</li>' for v in d.get('sources',[]));css='body{font:16px system-ui;max-width:900px;margin:auto;padding:48px;color:#151515}h1{font-size:44px}h2{margin-top:32px;color:#333}@media print{body{padding:0}}'
Path(x.output).write_text(f'<!doctype html><meta charset="utf-8"><style>{css}</style><h1>{html.escape(d["title"])}</h1><h2>Resumo executivo</h2><p>{html.escape(d["summary"])}</p><h2>Recomendações</h2><ol>{items}</ol><h2>Fontes</h2><ul>{src}</ul>')
