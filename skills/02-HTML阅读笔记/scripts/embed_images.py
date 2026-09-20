#!/usr/bin/env python3
import base64,mimetypes,os,re,sys
def uri(p):
    mime=mimetypes.guess_type(p)[0] or "application/octet-stream"
    return "data:%s;base64,%s"%(mime,base64.b64encode(open(p,"rb").read()).decode())
def main(src):
    base=os.path.dirname(os.path.abspath(src)); html=open(src,encoding="utf-8").read(); missing=[]
    def r1(m):
        p=os.path.join(base,m.group(1))
        if os.path.exists(p): return 'src="'+uri(p)+'"'
        missing.append(m.group(1)); return m.group(0)
    html=re.sub(r'src="(assets/[^"]+)"',r1,html)
    def r2(m):
        p=os.path.join(base,m.group(1))
        if os.path.exists(p): return 'url("'+uri(p)+'")'
        missing.append(m.group(1)); return m.group(0)
    html=re.sub(r'url\("?((?:assets/)[^")]+)"?\)',r2,html)
    if missing: print("Missing:",missing,file=sys.stderr); return 1
    out=os.path.splitext(src)[0]+"_embed.html"; open(out,"w",encoding="utf-8").write(html); print(out); return 0
if __name__=="__main__": sys.exit(main(sys.argv[1]))
