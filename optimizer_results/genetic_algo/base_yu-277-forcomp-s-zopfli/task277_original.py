B=any
A=range
def p(g):
 t=[]
 for y in A(10):
  for x in A(10):u=[(0,0)];u=[(i-y,j-x)for i in A(10)for j in A(10)if g[i][j]==8if B((i-y-a)**2+(j-x-b)**2<1for(a,b)in u)];u=[(i-y,j-x)for i in A(10)for j in A(10)if g[i][j]==8if B((i-y-a)**2+(j-x-b)**2<3for(a,b)in u)];u=[(i-y,j-x)for i in A(10)for j in A(10)if g[i][j]==8if B((i-y-a)**2+(j-x-b)**2<3for(a,b)in u)];u=[(i-y,j-x)for i in A(10)for j in A(10)if g[i][j]==8if B((i-y-a)**2+(j-x-b)**2<3for(a,b)in u)];t+=[(i-y,j-x)for i in A(10)for j in A(10)if g[i][j]==8if B((i-y-a)**2+(j-x-b)**2<3for(a,b)in u)],
 return[[(t[y*10+x]>[])*(3-t.count(t[y*10+x]))for x in A(10)]for y in A(10)]