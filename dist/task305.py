A=enumerate
def p(g):
 k=max(map(max,g))
 for(i,r)in A(g):
  for(j,_)in A(r):r[j]=(i+j)%k+1
 return g