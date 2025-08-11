def p(g):
 m,n=len(g),len(g[0])
 for r in range(m):
  J=[j for j in range(n)if g[r][j]]
  if len(J)>1:
   j0=J[0];l=len(J);h=[g[r][j0+i]for i in range(l)]
   c=next(j for j in J if (r and g[r-1][j])or(r+1<m and g[r+1][j]))
   v=[g[i][c]for i in range(m)if g[i][c]];a=min(i for i in range(m)if g[i][c])
   for i in range(m):g[i][c]=v[(i-a)%len(v)]
   for j in range(n):g[r][j]=h[(j-j0)%l]
   break
 return g
