A=enumerate
def p(g):
 r,c={},set()
 for(i,a)in A(g):
  for(j,v)in A(a):
   if v&1:r[i]=v
   elif v:c|={j}
 return[[r.get(i)or(j in c)*2for(j,_)in A(g[0])]for(i,_)in A(g)]