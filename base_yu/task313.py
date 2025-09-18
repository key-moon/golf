# best: 63(jailctf merger) / others: 64(4atj sisyphus luke Seek mukundan), 65(ox jam), 65(xsot ovs att joking mewheni), 71(kabutack), 71(intgrah jimboko awu macaque sammyuri)
# ============================= 63 ============================
# p=lambda g:(R:=range(len(g)))and[[g[i%(3-(g[0]==g[2]))][j%(3-(g[0][0]==g[0][2]))+1]for j in R] for i in R]
# p=lambda g:(R:=range(n:=len(g)),u:=(n>11)*4+2)and[[g[i%u][(j+1)%u]for j in R]for i in R]
# p=lambda g:(n:=len(g),u:=(n>11)*4+2)and[((s[1:u]+s[:1])*9)[:n]for s in(g[:u]*9)[:n]]
# p=lambda g:(n:=len(g),u:=(n>11)*4+2)and[(s[:u]*9)[1:n+1]for s in(g[:u]*9)[:n]]

def p(g):
 n=len(g)
 u=(n>11)*4+2
 return[(s[:u]*9)[1:n+1]for s in(g[:u]*9)[:n]]


# def p(g):
#  n,x,y=len(g),3-(g[0][0]==g[0][2]),3-(g[0][0]==g[2][0])
#  R=range(n)
#  for i in R:
#   s=g[i]=g[i][1:]+[g[i][-1]]
#   for j in R:
#    if s[j]==g[-1][-1]:s[j]=g[i%y][j%x]
#  return g

# def p(g):
#  n=len(g)
#  x=g[0][0]==g[0][2]
#  y=g[0][0]==g[2][0]
#  for i in range(n):
#   g[i]=g[i][1:]+[g[i][-1]]
#   for j in range(n):
#    if g[i][j]==g[-1][-1]:
#     g[i][j]=g[i%(3-y)][j%(3-x)]
#  return g
