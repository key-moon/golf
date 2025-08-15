F=enumerate
def p(g):
 for G in set(sum(g,[])):
  A=[(i,j)for(i,r)in F(g)for(j,v)in F(r)if v==G];B,C=min(A);D,E=max(A)
  if D-B>1<E-C and all(i in(B,D)or j in(C,E)for(i,j)in A):return[r[C+1:E]for r in g[B+1:D]]