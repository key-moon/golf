def p(g,u=range):
 s=[r[:]for r in g]
 for c in u(1,10):
  Q=[(i,j)for i in u(len(g))for j in u(len(g[0]))if g[i][j]==c]
  for i in u(len(Q)):
   for j in u(i+1,len(Q)):
    T,e=Q[i]
    R,J=Q[j]
    if T==R:
     for x in u(min(e,J),max(e,J)+1):s[T][x]=c
    elif e==J:
     for y in u(min(T,R),max(T,R)+1):s[y][e]=c
 return s