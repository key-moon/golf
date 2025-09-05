def p(g,z=range):
 r,c=len(g),len(g[0])
 b=[]
 for i in z(r-1):
  for j in z(c-1):
   a=g[i][j],g[i][j+1],g[i+1][j],g[i+1][j+1]
   if all(a):b+=[(i,j,len(set(a)))]
 for i,j,n in b:
  for k in z(n):
   x=i+2+k
   if x<r:g[x][j]=g[x][j+1]=3
 return g