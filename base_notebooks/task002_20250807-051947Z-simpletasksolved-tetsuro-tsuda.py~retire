def p(g):
 R=range
 n=len(g);v=[[0]*n for _ in R(n)]
 def f(i,j):
  if 0<=i<n and 0<=j<n and not v[i][j] and g[i][j]==0:v[i][j]=1;[f(i+d,j+e)for d,e in[(1,0),(-1,0),(0,1),(0,-1)]]
 [f(i,0)or f(i,n-1)or f(0,i)or f(n-1,i)for i in R(n)]
 return[[4 if g[i][j]==0 and not v[i][j]else g[i][j]for j in R(n)]for i in R(n)]