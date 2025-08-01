def p(g):
 a,b=len(g),len(g[0]);s=[(i,j,g[i][j])for i in range(a)for j in range(b)if g[i][j]]
 for i in range(a):
  for j in range(b):
   d=[max(abs(i-x),abs(j-y))for x,y,_ in s];d.sort();m=d[0]
   g[i][j]=s[d.index(m)][2]if m<d[1]and m%2<1 else 0
 return g
