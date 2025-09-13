# best: 162(biz) / others: 170(4atj sisyphus luke Seek mukundan), 172(Yuchen20), 173(jailctf merger), 174(dbdr), 176(xsot ovs att joking mewheni)
# ============================================================================= 162 ==============================================================================
import re
def p(g):
 c=len({*str(g)})-5
 f=lambda s:sum([[v*0!=0and f(v)or v]*c for v in s],[])
 t=f(g)
 n=len(t)*3
 for _ in range(4):
  t=[*zip(*eval(re.sub("0(?=(.{%d})*, 0.{%d}0, [13-9])"%(n+5,n-2),"2",str(t)))[::-1])]
 return t
