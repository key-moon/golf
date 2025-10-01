def p(g):
 t=[]
 for y in range(10):
  for x in range(10):u=[(0,0)];u=[(i-y,j-x)for i in range(10)for j in range(10)if g[i][j]==8if any((i-y-a)**2+(j-x-b)**2<1for(a,b)in u)];u=[(i-y,j-x)for i in range(10)for j in range(10)if g[i][j]==8if any((i-y-a)**2+(j-x-b)**2<3for(a,b)in u)];u=[(i-y,j-x)for i in range(10)for j in range(10)if g[i][j]==8if any((i-y-a)**2+(j-x-b)**2<3for(a,b)in u)];u=[(i-y,j-x)for i in range(10)for j in range(10)if g[i][j]==8if any((i-y-a)**2+(j-x-b)**2<3for(a,b)in u)];t+=[(i-y,j-x)for i in range(10)for j in range(10)if g[i][j]==8if any((i-y-a)**2+(j-x-b)**2<3for(a,b)in u)],
 return[[(t[y*10+x]>[])*(3-t.count(t[y*10+x]))for x in range(10)]for y in range(10)]