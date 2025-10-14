# best: 125(4atj sisyphus luke Seek mukundan) / others: 128(jailctf merger), 129(ox jam), 175(import itertools), 187(2F), 187(biz)
# =========================================================== 125 ===========================================================

import re
p=lambda g,c=-3:c*g or [*zip(*eval(re.sub("0(?=(.{29}, 0)*(, 0){0,2}.{25}0, 2|, 2.{28}[^0])|(?!=[^20], )2(?=, [^20].{25}[^0])",str(sum({*sum(g,[])})-2),str(p(g,c+1))))[::-1])]

# def p(g):
#  u=sum(g,[])
#  Y,X=divmod(u.index(max(u,key=bool)),9)
#  return[[sum({*u}-{2})*(v>0 or g[Y+(r>Y)][X+(c>X)]==2>min(abs(r-c-Y+X),abs(r+c-Y-X-1)))for c,v in enumerate(R)]for r,R in enumerate(g)]
