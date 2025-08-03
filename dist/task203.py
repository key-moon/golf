def p(g):
 n=len(g);a=[g[i][i]for i in range((n+1)//2)]
 for i in range(n):
  for j in range(n):g[i][j]=a[-1-min(i,j,n-1-i,n-1-j)]
 return g