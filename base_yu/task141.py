# best: 94(jailctf merger) / others: 96(4atj sisyphus luke Seek mukundan), 100(natte), 106(xsot ovs att joking mewheni), 112(MasukenSamba), 115(Bulmenisaurus)
# ============================================ 94 ============================================
# p=lambda g:(R:=range(len(g)))and[[max((y-x==i-j or y+x==i+j)*(g[i][j]|g[y][x])for y in R for x in R)for j in R]for i in R]
# p=lambda g:(R:=range(len(g)))and[[max((y-i in(x-j,j-x))*g[y][x]for y in R for x in R)for j in R]for i in R]
# p=lambda g:(R:=range(len(g)))and[[max(g[k][j+i-k]+g[k][j-i+k]for k in R)for j in R]for i in R]
# p=lambda g:(R:=range(len(g)))and[[max(0<j+(i-k)*s<len(g)and g[k][j+(i-k)*s]for s in(1,-1)for k in R)for j in R]for i in R]

def p(g):
 R=range(len(g))
 return[[max((y-i in(x-j,j-x))*g[y][x]for y in R for x in R)for j in R]for i in R]


# def p(g):
#  u=sum(g,[])
#  R=range(n:=len(g))
#  y,x=divmod(u.index(c:=max(u)),n)
#  return [[(y-x==i-j or y+x==i+j)*c for j in R]for i in R]




