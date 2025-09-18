def p(g):
 a,b=len(g),len(g[0])
 z=[(i,j)for i in range(a)for j in range(b)if g[i][j]==0]
 y=min(i for i,j in z);x=min(j for i,j in z);s=max(i for i,j in z)-y+1
 for t in range(1,a+1):
  if all(g[i][j]==g[i%t][j%t]for i in range(a)for j in range(b)if g[i][j]):break
 return[[g[(y+r)%t][(x+c)%t]for c in range(s)]for r in range(s)]