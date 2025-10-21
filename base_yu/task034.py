# best: 125(Code Golf International, 4atj sisyphus luke Seek mukundan) / others: 128(jailctf merger), 129(ox jam), 161(import itertools), 187(2F), 187(biz)
# =========================================================== 125 ===========================================================

# import re
# p=lambda g,c=-3:c*g or [*zip(*eval(re.sub("0(?=(.{29}, 0)*(, 0){0,2}.{25}0, 2|, 2.{28}[^0])|(?!=[^20], )2(?=, [^20].{25}[^0])",str(sum({*sum(g,[])})-2),str(p(g,c+1))))[::-1])]

import re;p=lambda g,c=-3:c*g or[*zip(*eval(re.sub("(?=(.{29})?(...)?(.{32})*2.{28}[^0], [^0])\d","(a:=max(max(g)))-3%a%3",str(p(g,c+1))))[::-1])]

# import re
# def p(g):
# #  g=eval(re.sub("0(?=(.{29})?(.{32})*.{31}[1-9].{31}[1-9])","1",str(g)))
#  for _ in range(4):
# #   g=eval(re.sub("(?=(.{0}|.{3}|.{29}|.{32}|.{35}|.{61}|.{64}|.{67}|.{93}|.{96}|.{99}|.{125}|.{128}|.{131})2.{28}[1-9], [1-9])\d","max(max(g))",str(g)))
#   # v="|".join(f".{{{v}}}" for v in sum([[i*32-3, i*32, i*32+3] for i in range(7)], [])[1:])
#   # g=eval(re.sub("(?=("+v+")2.{28}[1-9], [1-9])\d","(a:=max(max(g)))-3%a%3",str(g)))
#   g=eval(re.sub("(?=(.{29})?(...)?(.{32})*2.{28}[^0], [^0])\d","(a:=max(max(g)))-3%a%3",str(g)))
#   g=[*zip(*g[::-1])]
#  return g




# def p(g):
#  u=sum(g,[])
#  Y,X=divmod(u.index(max(u,key=bool)),9)
#  return[[sum({*u}-{2})*(v>0 or g[Y+(r>Y)][X+(c>X)]==2>min(abs(r-c-Y+X),abs(r+c-Y-X-1)))for c,v in enumerate(R)]for r,R in enumerate(g)]
