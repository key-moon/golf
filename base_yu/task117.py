# best: 148(4atj sisyphus luke Seek mukundan, jailctf merger) / others: 172(xsot ovs att joking mewheni), 211(natte), 229(MasukenSamba), 242(Potatoman), 242(jacekwl Potatoman nauti)
# ====================================================================== 148 =======================================================================


R=range
def p(g):
 n=len(g)
 for i in R(n-2,0,-1):
  for j in R(n):
   if[1]<[g[i][j]]*4==g[i-1][j-1:j+2:2]+g[i+1][j-1:j+2:2]:
    for z in R(n*n*2):
     if g[y:=z//n%n][x:=z%n]:g[i*2-y][x]=g[y][j*2-x]=g[y][x]
    return g


# R=range
# def p(g):
#  n=len(g)
#  for c in range(10):
#   u=[i for i,v in enumerate(sum(g,[]))if c==v]
#   if len(u)==5 and sum(u)==u[2]*5:
#    i,j=divmod(u[2],n)
#    for z in R(n*n*2):
#     if 0<g[y:=z//n%n][x:=z%n]!=g[i][j]:g[i*2-y][x]=g[y][j*2-x]=g[y][x]
#    return g

#  for i in R(n-2,0,-1):
#   for j in R(1,n-1):
#    if 0<g[i][j]==g[i+1][j+1]==g[i+1][j-1]==g[i-1][j+1]==g[i-1][j-1]:
#     for z in R(n*n*2):
#      if 0<g[y:=z//n%n][x:=z%n]!=g[i][j]:g[i*2-y][x]=g[y][j*2-x]=g[y][x]
#     return g

# R=range
# def p(g):
#  n=len(g)
#  for i in R(n-2,0,-1):
#   for j in R(1,n-1):
#    if 0<g[i][j]==g[i+1][j+1]==g[i+1][j-1]==g[i-1][j+1]==g[i-1][j-1]:
#     for z in R(n*n*2):
#      if 0<g[y:=z//n%n][x:=z%n]!=g[i][j]:g[i*2-y][x]=g[y][j*2-x]=g[y][x]
#     return g

# def p(g):
#  n=len(g)
#  for i in range(1,n-1)[::-1]:
#   for j in range(1,n-1):
#    if g[i][j]==g[i+1][j+1]==g[i+1][j-1]==g[i-1][j+1]==g[i-1][j-1]>0:
#     for y in range(n):
#      for x in range(n):
#       if 0<g[y][x]!=g[i][j]:
#        g[i*2-y][x]=g[y][j*2-x]=g[i*2-y][j*2-x]=g[y][x]
#     return g











