#!/usr/bin/env python3
import argparse,json
from pathlib import Path
a=argparse.ArgumentParser();a.add_argument('--input',required=True);a.add_argument('--output',required=True);x=a.parse_args();d=json.loads(Path(x.input).read_text());r=float(d['revenue']);c=float(d['variable_cost']);f=float(d['fixed_cost']);growth=d.get('growth',[-.1,0,.1]);o=[]
for g in growth: rev=r*(1+float(g)); contribution=rev-c*(1+float(g));o.append({'growth':g,'revenue':rev,'contribution':contribution,'result':contribution-f,'margin':(contribution/rev if rev else 0)})
Path(x.output).write_text(json.dumps({'scenarios':o},indent=2))
