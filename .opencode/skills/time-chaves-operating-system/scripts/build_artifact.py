#!/usr/bin/env python3
import argparse,json,pathlib,sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
def load(name):
 p=ROOT/name
 try: return json.loads(p.read_text())
 except Exception as e: raise SystemExit(f"resource error {name}: {e}")
def fail(message): raise SystemExit(message)
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--input",required=True); ap.add_argument("--output",required=True); ns=ap.parse_args()
 try: request=json.loads(pathlib.Path(ns.input).read_text())
 except Exception as e: fail(f"invalid input: {e}")
 if not isinstance(request,dict) or not request.get("objective") or not str(request["objective"]).strip(): fail("objective required")
 A=load("assets/agents.json"); B=load("assets/fes-contract.json")
 agents=A["agents"]; fes=B
 ids=[a["id"] for a in agents]
 if len(ids)!=len(set(ids)) or "main" not in ids: fail("agent roster invalid")
 if fes["states"][0]!="NOVA" or fes["states"][-1]!="CONCLUIDA" or len(fes["required"])<5: fail("FES contract invalid")
 transitions={s:[fes["states"][i+1]] if i+1<len(fes["states"]) else [] for i,s in enumerate(fes["states"])}
 transitions["EM_EXECUCAO"].append("BLOQUEADA"); transitions["BLOQUEADA"]=["EM_EXECUCAO"]
 artifact={"kind":"time-chaves-os","roster":agents,"task_schema":{"required":fes["required"],"states":fes["states"]},"state_machine":transitions,"invariants":["one_owner","evidence_before_done","external_write_requires_approval"]}
 artifact["objective"]=request["objective"].strip(); artifact["resources"]=["assets/agents.json","assets/fes-contract.json"]
 out=pathlib.Path(ns.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(artifact,ensure_ascii=False,indent=2)+"\n")
if __name__=="__main__": main()
