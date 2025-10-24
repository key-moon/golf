# best: 143(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II, biz) / others: 161(Tony Li), 161(Tony Li & Darren Amadeus Martin), 168(import itertools), 170(Code Golf International), 170(4atj sisyphus luke Seek mukundan)
# ==================================================================== 143 ====================================================================
import re
def p(g):
 c=len({*str(g)})-5
 t=sum([c*[sum(zip(*[s]*c),())]for s in g],[])
 n=len(t)*3
 for _ in'1'*4:
  t=[*zip(*eval(re.sub("0(?=(.{%d})*, 0.{%d}0, [^02])"%(n+5,n-2),"2",str(t)))[::-1])]
 return t
