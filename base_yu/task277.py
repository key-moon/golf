# best: 164(jailctf merger) / others: 189(intgrah jimboko awu macaque sammyuri), 194(4atj sisyphus luke Seek mukundan), 194(ox jam), 241(THUNDER THUNDER), 243(jacekw Potatoman nauti natte)
# ============================================================================== 164 ===============================================================================
def p(g):
 t=[]
 for y in range(10):
  for x in range(10):
   u=[(0,0)]
   u=[(i-y,j-x)for i in range(10)for j in range(10)if g[i][j] if any((i-y-a)**2+(j-x-b)**2<1 for a,b in u)]
   u=[(i-y,j-x)for i in range(10)for j in range(10)if g[i][j] if any((i-y-a)**2+(j-x-b)**2<3 for a,b in u)]
   u=[(i-y,j-x)for i in range(10)for j in range(10)if g[i][j] if any((i-y-a)**2+(j-x-b)**2<3 for a,b in u)]
   u=[(i-y,j-x)for i in range(10)for j in range(10)if g[i][j] if any((i-y-a)**2+(j-x-b)**2<3 for a,b in u)]
   t+=[(i-y,j-x)for i in range(10)for j in range(10)if g[i][j] if any((i-y-a)**2+(j-x-b)**2<3 for a,b in u)],
 return [[(t[y*10+x]>[])*(3-t.count(t[y*10+x]))for x in range(10)]for y in range(10)]
