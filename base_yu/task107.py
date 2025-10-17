# best: 161(Tony Li) / others: 162(biz), 168(import itertools), 170(jailctf merger), 170(4atj sisyphus luke Seek mukundan), 171(Yuchen20)
# ============================================================================= 161 =============================================================================
import re
def p(g):
 c=len({*str(g)})-5
 t=sum([c*[sum(zip(*[s]*c),())]for s in g],[])
 n=len(t)*3
 for _ in'1'*4:
  t=[*zip(*eval(re.sub("0(?=(.{%d})*, 0.{%d}0, [^02])"%(n+5,n-2),"2",str(t)))[::-1])]
 return t
