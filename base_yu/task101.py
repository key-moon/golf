# best: 281(xsot ovs att joking mewheni) / others: 315(jailctf merger), 349(4atj sisyphus luke Seek mukundan), 395(jacekwl Potatoman nauti), 402(MasukenSamba), 441(jonas ryno kg583)
def p(g):
 h=len(g)
 w=len(g[0])
 u=[]
 u=[(i,j)for i in range(h)for j in range(w)if g[i][j] == 2 and any(h>i+k>-1<j+l<w and (g[i+k][j+l]==1 or (i+k,j+l) in u) for k in range(-1,2) for l in range(-1,2))]
 u=[(i,j)for i in range(h)for j in range(w)if g[i][j] == 2 and any(h>i+k>-1<j+l<w and (g[i+k][j+l]==1 or (i+k,j+l) in u) for k in range(-1,2) for l in range(-1,2))]
 c=[]
 for i in range(h):
  c+=[0]*w,
  for j in range(w):
   if g[i][j]==2 and (i,j) not in u:
    c[i][j]=max(c[i-1][j], c[i][j-1])
    while j+c[i][j]<w and i+c[i][j]<h and g[i][j+c[i][j]]==g[i+c[i][j]][j]==2:
     c[i][j]+=1
 return[[g[y][x] or any(g[i][j]==1 and all(h>y+(a-i)*s>-1<x+(b-j)*s<w and c[y+(a-i)*s][x+(b-j)*s]==s for a,b in u)for i in range(h)for j in range(w)for s in range(1,4))for x in range(w)]for y in range(h)]
