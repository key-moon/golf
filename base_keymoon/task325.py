# 連結成分の個数がほしい
import re
def p(g):
 d=re.sub("[[ ,]","",str(g))
 n=[8]
 while"8"in d:
  d=re.sub("8","1",d,1)
  for x in d:
   d=re.sub("8(?=("+"."*len(g[0])+")?1)","1",d)[::-1]
  n+=[0]
 # ここ割と適当 改善の余地あるかも
 return [(n:=[0,*n[:-1]])[1:]for x in n[:-1]]