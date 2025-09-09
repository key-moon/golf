# best: 218(natte, 2F, biz) / others: 230(xsot ovs att joking mewheni), 243(jailctf merger), 261(4atj sisyphus luke Seek mukundan), 285(kdmitrie), 286(jacekwl Potatoman nauti)
#上下の囲み+左右方向の破線を書く→90度回転

def p(g):
 u=[s[:]for s in g]
 for _ in range(2):
  for i in range(len(g)):
   if a:=[j for j in range(len(g[i]))if g[i][j]]:
    j,k=a
    for t in range(j-1,j+2):u[i-1][t]=u[i+1][t]=g[i][k]
    for t in range(k-1,k+2):u[i-1][t]=u[i+1][t]=g[i][j]
    for t in range(j+2,k-1):u[i][t]=min(t-j-1,k-1-t)%2*5
  *g,=zip(*g)
  *u,=map(list,zip(*u))
 return u


# R=range
# def p(g):
#  u=[s[:]for s in g]
#  for _ in 0,1:
#   for i in R(len(g)):
#    if a:=[j for j in R(len(g[0]))if (s:=g[i])[j]]:
#     j,k=a
#     l,r=u[i-1],u[i+1]
#     l[j-1:j+2]=r[j-1:j+2]=[s[k]]*3
#     l[k-1:k+2]=r[k-1:k+2]=[s[j]]*3
#     for t in R(j+2,k-1):u[i][t]=-~min(t-j,k-t)%2*5
#   *g,=zip(*g)
#   *u,=map(list,zip(*u))
#  return u






