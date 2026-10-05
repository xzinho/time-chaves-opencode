#!/usr/bin/env python3
import argparse,json
from pathlib import Path
a=argparse.ArgumentParser();a.add_argument('--input',required=True);a.add_argument('--output',required=True);x=a.parse_args();d=json.loads(Path(x.input).read_text());dims=['concept','hierarchy','typography','color','composition','consistency','responsive','wcag','performance','brand_fit'];scores={k:int(d.get(k,0)) for k in dims};
if any(v<0 or v>5 for v in scores.values()): raise SystemExit('scores must be 0..5')
total=sum(scores.values());critical=scores['wcag']<3 or scores['hierarchy']<3;Path(x.output).write_text(json.dumps({'scores':scores,'total':total,'max':50,'gate':'PASS' if total>=40 and not critical else 'FAIL','critical':critical},indent=2))
