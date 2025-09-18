def p(g):
 R,c=next((i,j)for i,x in enumerate(g)for j,v in enumerate(x)if v==7);m=0
 while R+m<len(g)and g[R+m][c]==7:m+=1
 for k in range(m):
  a=c-m+k+1
  for j in range(a,c+m-k):g[R+k][j]=(8,7)[(k+j-a)%2]
 return g
