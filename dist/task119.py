def p(g):
 for I in range(4800):
  u,v=I%2*2-1,(I&2)-1
  if g[i:=I//40%10+1][j:=I//4%10+1]>2and g[i+u][j+v]>2:
   s=g[i+u*~-(g[i-u][j]&2)]
   s[w]=s[w:=j+v*~-(g[i][j-v]&2)]or 3
 return g