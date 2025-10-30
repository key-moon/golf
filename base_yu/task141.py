# best: 93(jailctf merger, ox jam) / others: 96(Code Golf International), 96(4atj sisyphus luke Seek mukundan), 100(jacekw Potatoman nauti natte), 100(natte), 100(import itertools)
# ============================================ 93 ===========================================
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
