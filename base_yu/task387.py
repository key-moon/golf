# best: 202(jailctf merger) / others: 215(jacekw Potatoman nauti natte), 215(import itertools), 218(natte), 218(2F), 225(biz)
#上下の囲み+左右方向の破線を書く→90度回転

# def p(g):
#  u=[s[:]for s in g]
#  for _ in range(2):
#   for i in range(len(g)):
#    if a:=[j for j in range(len(g[i]))if g[i][j]]:
#     j,k=a
#     for t in range(j-1,j+2):u[i-1][t]=u[i+1][t]=g[i][k]
#     for t in range(k-1,k+2):u[i-1][t]=u[i+1][t]=g[i][j]
#     for t in range(j+2,k-1):u[i][t]=min(t-j-1,k-1-t)%2*5
#   *g,=zip(*g)
#   *u,=map(list,zip(*u))
#  return u

# def p(g):
#  for _ in range(2):
#   for i in range(len(g)):
#    if len(a:=[j for j in range(len(g[i]))if g[i][j]%5]) == 2:
#     j,k=a
#     for t in range(i-1,i+2):
#      g[t][j-1]=g[t][j+1]=g[i][k]
#      g[t][k-1]=g[t][k+1]=g[i][j]
#     for t in range(j+2,k-1):g[i][t]=min(t-j-1,k-1-t)%2*5
#   *g,=map(list,zip(*g))
#  return g


def p(g):
 for _ in range(2):
  for i in range(len(g)):
   if len(a:=[j for j in range(len(g[i]))if g[i][j]%5])==2:
    j,k=a
    for t in range(i-1,i+2):
     *g[t],=g[t]
     g[t][j-1]=g[t][j+1]=g[i][k]
     g[t][k-1]=g[t][k+1]=g[i][j]
    for t in range(j+2,k-1):g[i][t]=min(t-j-1,k-1-t)%2*5
  *g,=zip(*g)
 return g



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
