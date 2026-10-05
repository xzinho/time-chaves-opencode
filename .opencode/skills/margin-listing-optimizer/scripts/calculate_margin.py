#!/usr/bin/env python3
import argparse,json
from pathlib import Path
a=argparse.ArgumentParser();a.add_argument('--input',required=True);a.add_argument('--output',required=True);x=a.parse_args();d=json.loads(Path(x.input).read_text());p=float(d['price']);costs=sum(float(d.get(k,0)) for k in ['cogs','fixed_fee','shipping','tax','ads','packaging','returns','financial_cost']);costs+=p*float(d.get('commission_rate',0));m=p-costs;Path(x.output).write_text(json.dumps({'price':p,'total_cost':costs,'net_margin':m,'net_margin_rate':m/p if p else 0},indent=2))
