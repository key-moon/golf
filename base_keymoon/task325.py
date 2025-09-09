# best: 160(jailctf merger) / others: 161(4atj sisyphus luke Seek mukundan), 172(xsot ovs att joking mewheni), 217(natte), 217(jacekwl), 217(jacekwl Potatoman nauti)
# ============================================================================ 160 =============================================================================
# 連結成分の個数がほしい ref: base_keymoon/task048.py
import re;s=re.sub
def p(g):
 d=s("[[ ,]","",str(g))
 n=[8]
 while"8"in d:
  d=s("8","1",d,1)
  for x in d:
   d=s("8(?=("+"."*len(g[0])+")?1)","1",d)[::-1]
  n+=[0]
 # ここ割と適当 改善の余地あるかも
 return [(n:=[0,*n[:-1]])[1:]for x in n[:-1]]




