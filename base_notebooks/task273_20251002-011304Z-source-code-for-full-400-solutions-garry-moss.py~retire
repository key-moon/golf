l=enumerate
r=range
def p(u):
 u=[e[:]for e in u];f=[[e for(e,f)in l(e)if f==4]for e in u]
 for(q,m)in l(f):
  for(f,e)in l(m):
   for f in m[f+1:]:
    for p in r(q+1,len(u)):
     if u[p][e]==4and u[p][f]==4:
      for p in r(q+1,p):u[p][e+1:f]=[2]*(f-e-1)
 return u