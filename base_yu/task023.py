# best: 195(4atj sisyphus luke Seek mukundan) / others: 199(jailctf merger), 204(cubbus), 206(ox jam), 230(intgrah jimboko awu macaque sammyuri), 232(jacekw Potatoman nauti natte)
# ============================================================================================== 195 ==============================================================================================
import re
def p(g):
 g=[g[-1]]+g
 for _ in[0]*8:
  for _ in[0]*7:
   d=re.sub("[[ ,]","",str(g))
   d=re.sub(f"(?<=[^5]{'.'*(len(g[0])-2)}.[^5])555(?={'.'*(len(g[0])-2)}[^5])","222",d)
   g=[[*map(int,c)]for c in d.split("]")[:-2]]
   *g,=map(list,zip(*g[::-1]))
  d=re.sub("[[ ,]","",str(g))
  d=re.sub(f"(?<=[^5]{'.'*(len(g[0])-2)}.[^5])55({'.'*(len(g[0])-2)}.)55(?=[^5]{'.'*(len(g[0])-2)}.[^5])","88\\g<1>88",d)
  g=[[*map(int,c)]for c in d.split("]")[:-2]]
 return g[1:]
