def p(g):
 n,len0=len(g),len(g[0])
 p=[(i,j)for i in range(n)for j in range(len0)if g[i][j]==2]
 a,b=min(i for i,j in p),min(j for i,j in p)
 s=[(i-a,j-b)for i,j in p]
 for i,j in p:g[i][j]=0
 for x in range(n):
  for y in range(len0):
   if(x,y)!=(a,b)and all(0<=x+u<n and 0<=y+v<len0 and g[x+u][y+v]==0 for u,v in s):
    for u,v in s:g[x+u][y+v]=2
    return g
 return g
