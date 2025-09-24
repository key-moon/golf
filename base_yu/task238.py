# best: 223(jailctf merger, ox jam) / others: 233(4atj sisyphus luke Seek mukundan), 260(natte), 264(intgrah jimboko awu macaque sammyuri), 265(jonas ryno kg583 kabutack), 265(JRKX)
def p(g):
 u=min(i for i in range(len(g)) for j in range(len(g[i]))if g[i][j]==8)
 v=min(j for i in range(len(g)) for j in range(len(g[i]))if g[i][j]==8)
 y=min(i for i in range(len(g)) for j in range(len(g[i]))if g[i][j]%8)
 x=min(j for i in range(len(g)) for j in range(len(g[i]))if g[i][j]%8)
 n=g[y][x+1:].index(0)
#  return [[g[u+i][v+j]and((i+j==n-1 or i==j)*8or g[y+(i+j>=n)*n+(i>j)][x+(i+j>=n)*n+(i<j)]) if n>i>-1<j<n else g[y+i+1][x+j+1] for j in range(-1,n+1)] for i in range(-1,n+1)]
#  return [[g[u+i-1][v+j-1]and((i+j==n+1 or i==j)*8or g[y+(i+j>n)*n+(i>j)][x+(i+j>n)*n+(i<j)]) if 0<i<n+1>j>0 else g[y+i][x+j] for j in range(n+2)] for i in range(n+2)]
 return [[0<i<n+1>j>0 and g[u-1+i][v-1+j]and((i+j==n+1 or i==j)*8or g[y+(i+j>n)*n+(i>j)][x+(i+j>n)*n+(i<j)])or g[y+i][x+j] for j in range(n+2)] for i in range(n+2)]


#  h=g
#  for _ in range(64):
#   h=[*zip(*h[({*h[-1],8}>{0,8})-2::-1])]
#  u=[[v for*t,v in zip(*g,s)if 8in t]for s in g if 8in s]
#  n=len(u)
#  return[h[0]]+[[h[1][0]]+[u[i][j]and((i+j==n-1 or i==j)*8 or[h[t:=i-j>0][1-t],h[t-2][~t]][i+j>=n]) for j in range(n)]+[h[1][-1]]for i in range(n)]+[h[-1]]




# R=range
# def p(g):
#  h=len(g);w=h*len(g[0]);s=[i for i in R(w)if g[i%h][i//h]==8];y,x=min(i%h for i in s),min(i//h for i in s)
# #  y=min(i for i in range(h) for j in range(w)if g[i][j]==8)
# #  x=min(j for i in range(h) for j in range(w)if g[i][j]==8)
#  for k in R(w):
#   if(i:=k%h)<h-1and len({g[i+1][j:=k//h],g[i][j],g[i][j+1]})>2:
#    m=g[i].index(0,j+1)-j-1;o=[g[i+l][j:j+m+2]for l in R(m+2)]
#    for c in R(m*m):
#     if g[y+(u:=c%m)][x+(v:=c//m)]:o[u+1][v+1]=(u+v==m-1 or u-v==0)and 8 or[o[t:=u-v>0][1-t],o[-2+t][-1-t]][u+v>=m]
#    #    o[u+1][v+1]=(u+v==m-1 or u-v==0)and 8 or [o[~(t:=u-v<0)][t-2],o[1-t][t]][u+v<m]
#    #    o[u+1][v+1]=(u+v==m-1 or u-v==0)and 8 or [o[1-(t:=u-v<0)][t],o[~t][t-2]][u+v>=m]
#    #    o[u+1][v+1]=(u+v==m-1 or u-v==0)and 8 or [o[t:=u-v>0][1-t],o[~(1-t)][(1-t)-2]][u+v>m]
#    return o


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
