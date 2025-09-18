def p(g):
 n,m=len(g),len(g[0])
 z=[(i,j)for i in range(n)for j in range(m)if g[i][j]==0]
 for k in set(sum(g,[]))-{0}:
  I=[i for i in range(n)if k in g[i]];J=[j for j in range(m)if any(g[i][j]==k for i in I)]
  a,b=I[0],I[-1];c,d=J[0],J[-1]
  R={i for i,j in z if a<=i<=b and c<=j<=d};C={j for i,j in z if a<=i<=b and c<=j<=d}
  if C and d-c>b-a:
   for i in range(a,b+1):
    for j in C:
     if g[i][j]==k:g[i][j]=0
  if R and b-a>=d-c:
   for i in R:
    for j in range(c,d+1):
     if g[i][j]==k:g[i][j]=0
 return g
