# best: 103(ox jam) / others: 104(jailctf merger), 105(Code Golf International), 106(lv1.dev), 108(LogicLynx), 109(4atj sisyphus luke Seek mukundan)
# ================================================ 103 ================================================
# port re;p=lambda g,c=-39:c*g or p([*zip(*eval(re.sub("0(?=(.{34}[1-9]){2,}, ([1-9]))","\\2",str(g)))[::-1])],c+1)
import re;p=lambda g,c=-39:c*g or p([*zip(*eval(re.sub("0(?=(.{34}([^0])){2,}, \\2)","\\2",str(g)))[::-1])],c+1)

# import re
# def p(g):
#  for _ in range(40):
# #   g=eval(re.sub("(%d, (%d.{34}){2,})0"%(c,c),"\\1 %d"%c,str(g)))
#   g=eval(re.sub("(([1-9]), (\\2.{34}){2,})0","\\1\\2",str(g)))
#   g=[*zip(*g[::-1])]
#  return g
