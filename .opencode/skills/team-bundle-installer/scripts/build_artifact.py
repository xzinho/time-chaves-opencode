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
 A=load("assets/bundle-manifest.json"); B=load("assets/security-policy.json")
 from pathlib import PurePosixPath
 files=A["files"]; policy=B; seen=set()
 for f in files:
     p=PurePosixPath(f["path"])
     if p.is_absolute() or ".." in p.parts or not any(str(p).startswith(r) for r in policy["allowed_roots"]): fail("unsafe bundle path")
     if str(p) in seen: fail("bundle path collision")
     seen.add(str(p))
     if len(f.get("sha256",""))!=64 or any(c not in "0123456789abcdef" for c in f["sha256"]): fail("invalid content hash")
     if f.get("mode") not in policy["file_modes"]: fail("unsafe permission")
 artifact={"kind":"transactional-install-plan","version":A["version"],"preflight":["verify_signature","verify_hashes","check_collisions"],"files":files,"rollback":{"authenticated":True,"restore_count":len(files)}}
 artifact["objective"]=request["objective"].strip(); artifact["resources"]=["assets/bundle-manifest.json","assets/security-policy.json"]
 out=pathlib.Path(ns.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(artifact,ensure_ascii=False,indent=2)+"\n")
if __name__=="__main__": main()
