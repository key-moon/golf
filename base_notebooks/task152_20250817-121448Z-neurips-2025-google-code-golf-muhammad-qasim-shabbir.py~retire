def p(N,F=range):
 n=len(N)
 o=[[0]*(2*n)for _ in F(2*n)]
 for i in F(n):
  for j in F(n):o[i][j]=N[i][j];o[i][2*n-j-1]=N[i][j];o[2*n-i-1][j]=N[i][j];o[2*n-i-1][2*n-j-1]=N[i][j]
 return o