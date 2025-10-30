# best: 195(Code Golf International, 4atj sisyphus luke Seek mukundan) / others: 197(jailctf merger), 204(cubbus), 206(ox jam), 225(import itertools), 228(jacekw Potatoman nauti natte)
# ============================================================================================== 195 ==============================================================================================
# import re
# def p(g):
#  for _ in range(12):
#   g=[[0,*s,0] for s in g]
#   for _ in range(12):
#    g=eval(re.sub("(?<=[028], )5(?=, [028])","1",str(g)))
#    g=eval(re.sub("[15], [15], 1(?=, [028])","2,2,2",str(g)))
#    g=eval(re.sub("(?<=[028], )[15], 1, [15](?=, [028])","2,2,2",str(g)))
#    g=[*zip(*g[::-1])]
#   g=eval(re.sub("5, 5(.{%d})5, 5(?=, [028].{%d}[028])"%(len(g[0])*3-2,len(g[0])*3-2),r"8,8\1 8,8",str(g)))
#   g=[*zip(*g[::-1])]
#   g=g[1:-1]
# #  g=eval(re.sub("5","8",str(g)))
#  return g

import re
def p(g):
 g=g[-1:]+g
 for _ in[0]*8:
  for _ in[0]*7:
   g[:]=zip(*eval(re.sub("([^5].{%d}([^5], |\())5, 5, 5(?=.{%d}[^5])"%(len(g[0])*3-2,len(g[0])*3-5),r"\1 2,2,2",str(g)))[::-1])
  g=eval(re.sub("(?<=[^5].{%d}[^5], )5, 5(.{%d})5, 5(?=, [^5].{%d}[^5])"%(len(g[0])*3-2,len(g[0])*3-2,len(g[0])*3-2),r"8,8\1 8,8",str(g)))
 return g[1:]

# import re
# def p(g):
#  g=[g[-1]]+g
#  for _ in[0]*8:
#   for _ in[0]*7:
#    d=re.sub("[[ ,]","",str(g))
#    d=re.sub(f"(?<=[^5]{'.'*(len(g[0])-1)}[^5])555(?={'.'*(len(g[0])-2)}[^5])","222",d)
#    g=[[*map(int,c)]for c in d.split("]")[:-2]]
#    return g
#    *g,=map(list,zip(*g[::-1]))
#   d=re.sub("[[ ,]","",str(g))
#   d=re.sub(f"(?<=[^5]{'.'*(len(g[0])-2)}.[^5])55({'.'*(len(g[0])-2)}.)55(?=[^5]{'.'*(len(g[0])-2)}.[^5])","88\\g<1>88",d)
#   g=[[*map(int,c)]for c in d.split("]")[:-2]]
#  return g[1:]
