#!/usr/bin/env python3
import os,sys
from PIL import Image
def compress(src,dst,max_w,quality):
    im=Image.open(src); w,h=im.size
    if w>max_w: h=round(h*max_w/w); w=max_w
    im.convert("RGB").resize((w,h),Image.LANCZOS).save(dst,quality=quality,optimize=True,progressive=True)
    return w,h,os.path.getsize(dst)
def main():
    a=sys.argv[1:]
    if not a: return 1
    os.makedirs("assets",exist_ok=True)
    print("assets/hero.jpg",compress(a[0],"assets/hero.jpg",1600,80))
    if len(a)>1: print("assets/cover.jpg",compress(a[1],"assets/cover.jpg",700,82))
if __name__=="__main__": sys.exit(main())
