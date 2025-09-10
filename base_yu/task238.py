# best: 223(jailctf merger, xsot ovs att joking mewheni) / others: 233(4atj sisyphus luke Seek mukundan), 265(jonas ryno kg583), 269(MasukenSamba), 275(natte), 314(kdmitrie)
R=range
def p(g):
 h=len(g);w=h*len(g[0]);s=[i for i in R(w)if g[i%h][i//h]==8];y,x=min(i%h for i in s),min(i//h for i in s)
#  y=min(i for i in range(h) for j in range(w)if g[i][j]==8)
#  x=min(j for i in range(h) for j in range(w)if g[i][j]==8)
 for k in R(w):
  if(i:=k%h)<h-1and len({g[i+1][j:=k//h],g[i][j],g[i][j+1]})>2:
   m=g[i].index(0,j+1)-j-1;o=[g[i+l][j:j+m+2]for l in R(m+2)]
   for c in R(m*m):
    if g[y+(u:=c%m)][x+(v:=c//m)]:o[u+1][v+1]=(u+v==m-1 or u-v==0)and 8 or[o[t:=u-v>0][1-t],o[-2+t][-1-t]][u+v>=m]
   #    o[u+1][v+1]=(u+v==m-1 or u-v==0)and 8 or [o[~(t:=u-v<0)][t-2],o[1-t][t]][u+v<m]
   #    o[u+1][v+1]=(u+v==m-1 or u-v==0)and 8 or [o[1-(t:=u-v<0)][t],o[~t][t-2]][u+v>=m]
   #    o[u+1][v+1]=(u+v==m-1 or u-v==0)and 8 or [o[t:=u-v>0][1-t],o[~(1-t)][(1-t)-2]][u+v>m]
   return o


# R=range
# def p(g):
#  h=len(g)
#  w=h*len(g[0])
#  s=[i for i in R(w)if g[i%h][i//h]==8]
#  y,x=min(i%h for i in s),min(i//h for i in s)
# #  y=min(i for i in range(h) for j in range(w)if g[i][j]==8)
# #  x=min(j for i in range(h) for j in range(w)if g[i][j]==8)
#  for k in R(w):
#   if(i:=k%h)<h-1and len({g[i+1][j:=k//h],g[i][j],g[i][j+1]})>2:
#    m=g[i].index(0,j+1)-j-1
#    o=[g[i+l][j:j+m+2]for l in R(m+2)]
#    for c in R(m*m):
#     if g[y+(u:=c%m)][x+(v:=c//m)]:o[u+1][v+1]=(u+v==m-1 or u-v==0)and 8 or[o[t:=u-v>0][1-t],o[-2+t][-1-t]][u+v>=m]
#    #    o[u+1][v+1]=(u+v==m-1 or u-v==0)and 8 or [o[~(t:=u-v<0)][t-2],o[1-t][t]][u+v<m]
#    #    o[u+1][v+1]=(u+v==m-1 or u-v==0)and 8 or [o[1-(t:=u-v<0)][t],o[~t][t-2]][u+v>=m]
#    #    o[u+1][v+1]=(u+v==m-1 or u-v==0)and 8 or [o[t:=u-v>0][1-t],o[~(1-t)][(1-t)-2]][u+v>m]
#    return o

# def p(g):
#  h,w=len(g),len(g[0])
#  y=min(i for i in range(h) for j in range(w)if g[i][j]==8)
#  x=min(j for i in range(h) for j in range(w)if g[i][j]==8)
#  for i in range(h):
#   for j in range(w-1):
#    if len({g[i+1][j],g[i][j],g[i][j+1]})==3:
#     m=g[i].index(0,j+1)-j-1
#     o=[g[i+l][j:j+m+2]for l in range(m+2)]
#     for u in range(m):
#      for v in range(m):
#       if g[y+u][x+v]:
#        if u+v==m-1 or u-v==0:
#         o[u+1][v+1]=8
#        else:
#         t=u-v<0
#         o[u+1][v+1]=[o[~t][t-2],o[1-t][t]][u+v<m]
#         # o[u+1][v+1]=[o[-1][1],o[1][-1],o[1][0],o[0][1]][(u+v<m)*2+(u-v<0)]
#     return o
#  return g

# def p(g):
#  h,w=len(g),len(g[0])
#  y=min(i for i in range(h) for j in range(w)if g[i][j]==8)
#  x=min(j for i in range(h) for j in range(w)if g[i][j]==8)
#  for i in range(h):
#   for j in range(w-1):
#    if len({g[i+1][j],g[i][j],g[i][j+1]})==3:
#     k=g[i].index(0,j+1)+1
#     m=k-j-2
#     o=[g[i+l][j:k] for l in range(k-j)]
#     for u in range(m):
#      for v in range(m):
#       if g[y+u][x+v]:
#        if u+v==m-1 or u-v == 0:
#         o[u+1][v+1]=8
#        else:
#         o[u+1][v+1]=[o[-1][1],o[1][-1],o[1][0],o[0][1]][(u+v<m)*2+(u-v<0)]
#     return o
#  return g











