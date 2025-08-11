def p(b,u=range):
 n=len(b)
 o=[[0]*(2*n)for _ in u(2*n)]
 for i in u(n):
  for j in u(n):o[i][j]=b[i][j];o[i][2*n-j-1]=b[i][j];o[2*n-i-1][j]=b[i][j];o[2*n-i-1][2*n-j-1]=b[i][j]
 return o