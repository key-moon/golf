# best: 288(jailctf merger) / others: 302(ox jam), 302(xsot ovs att joking mewheni), 318(natte), 332(intgrah jimboko awu macaque sammyuri), 362(MasukenSamba)
def p(g):
 for _ in range(8):
  for i in range(1,len(g)):
   for j in range(1,len(g)):
    if 3<len({g[i][j],g[i-1][j],g[i][j-1],g[i-1][j-1]}):
     u=[[0]*5 for _ in range(8)] # range(5) で十分ではある
     u[0][0]=1
     q=[(0,0)]
     while q:
      (y,x),*q=q
      g[i+y][j-1-x]|=g[i][j-1]
      g[i-1-y][j+x]|=g[i-1][j]
      for d in range(9):
       if 0<y+d%3<6 and 0<x+d//3<6 and 1-u[y+d%3-1][x+d//3-1]and 0<g[i+y+d%3-1][j+x+d//3-1]==g[i][j]:
        u[y+d%3-1][x+d//3-1]=1
        q+=[(y+d%3-1,x+d//3-1)]
  g[:]=map(list,zip(*g[::-1]))
  # *g,=map(list,zip(*g[::-1]))
 return g

# def p(g):
#  n=len(g)
#  for _ in range(8):
#   for i in range(n-1):
#    for j in range(n-1):
#     if len({g[i][j],g[i+1][j],g[i][j+1],g[i+1][j+1]})==4:
#      u=[[0]*6 for _ in range(6)]
#      u[0][0]=1
#      q=[(0,0)]
#      while q:
#       y,x=q.pop()
#       for d in range(9):
#        Y=y+d%3-1
#        X=x+d//3-1
#        if-1<Y<6 and-1<X<6 and 1-u[Y][X] and g[i+Y][j+X]==g[i+1][j+1]>0:
#         u[Y][X]=1
#         q+=[(Y,X)]
#         g[i+1-Y][j+X]|=g[i][j+1]
#         g[i+Y][j+1-X]|=g[i+1][j]
#   *g,=map(list,zip(*g[::-1]))
#  return g

# def p(g):
#  n=len(g)
#  for _ in range(8):
#   for i in range(n-1):
#    for j in range(n-1):
#     if len({g[i][j],g[i+1][j],g[i][j+1],g[i+1][j+1]})==4:
#      u=[[0]*6 for _ in range(6)]
#      u[0][0]=1
#      q=[(0,0)]
#      while q:
#       y,x=q.pop()
#       for d in range(9):
#        Y=y+d%3-1
#        X=x+d//3-1
#        if 0<=Y<6 and 0<=X<6 and not u[Y][X] and g[i+Y][j+X]==g[i+1][j+1]>0:
#         u[Y][X]=1
#         q.append((Y,X))
#         if g[i][j+1]>0:g[i+1-Y][j+X]=g[i][j+1]
#         if g[i+1][j]>0:g[i+Y][j+1-X]=g[i+1][j]
#   *g,=map(list,zip(*g[::-1]))
#  return g
