# best: 109(4atj sisyphus luke Seek) / others: 111(jailctf merger), 111(sisyphus), 112(natte), 112(joking MeWhenI), 119(Seek64)
# =================================================== 109 ===================================================
import re
p=lambda g,c=-39:c*g or p([*zip(*eval(re.sub("(([1-9]), (\\2.{34}){2,})0","\\1\\2",str(g)))[::-1])],c+1)


# import re
# def p(g):
#  for _ in range(40):
# #   g=eval(re.sub("(%d, (%d.{34}){2,})0"%(c,c),"\\1 %d"%c,str(g)))
#   g=eval(re.sub("(([1-9]), (\\2.{34}){2,})0","\\1\\2",str(g)))
#   g=[*zip(*g[::-1])]
#  return g
 
