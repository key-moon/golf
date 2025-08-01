def p(g):
 m,n=len(g),len(g[0])
 val2=[(i,j)for i in range(m)for j in range(n)if g[i][j]==2]
 val3=[(i,j)for i in range(m)for j in range(n)if g[i][j]==3]
 s=min(val3,key=lambda a:min(abs(a[0]-b[0])+abs(a[1]-b[1])for b in val2))
 t=min(val2,key=lambda b:abs(b[0]-s[0])+abs(b[1]-s[1]))
 dr=(t[0]>s[0])-(t[0]<s[0]); dc=(t[1]>s[1])-(t[1]<s[1])
 x,y=s
 while 0<=x+dr<m and g[x+dr][y]!=8:
  x+=dr; g[x][y]=3
 while 0<=y+dc<n and g[x][y+dc]!=8:
  y+=dc; g[x][y]=3
 return g
