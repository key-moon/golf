# 連結成分の個数がほしい ref: base_keymoon/task048.py
import re;s=re.sub
def p(g):
 d=s("[[ ,]","",str(g))
 for x in g+g:d=s("0(?=("+"."*len(g[0])+")?1)","1",d)[::-1]
 return [[*map(int,r)]for r in d.split("]")[:-2]]
