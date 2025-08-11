def p(X,k=range):
 n=len(X)
 o=[[0]*(2*n)for _ in k(2*n)]
 for i in k(n):
  for j in k(n):o[i][j]=X[i][j];o[i][2*n-j-1]=X[i][j];o[2*n-i-1][j]=X[i][j];o[2*n-i-1][2*n-j-1]=X[i][j]
 return o