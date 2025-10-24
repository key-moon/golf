a=range
c=len
def p(p):
 g,t=c(p),c(p[0]);f,o=[],[99,99,0,0];x=[f for f in sum(p,[])if f not in[0,2]][0]
 for u in a(g):
  e=p[u].count(2)
  if e>1and len(f)<1:f=[u,p[u].index(2),e]
  e=p[u].count(x)
  if e>0:
   o[0]=min([u,o[0]])
   for t in a(t):
    if p[u][t]==x:o[1]=min([t,o[1]])
 e=f[2]//3
 for u in a(3):
  for t in a(3):
   for l in a(e):
    for n in a(e):p[f[0]+u*e+l+1][f[1]+t*e+n+1]=p[o[0]+u][o[1]+t]
 p=p[f[0]:f[0]+f[2]];p=[u[f[1]:f[1]+f[2]]for u in p];return p