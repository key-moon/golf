def p(g):
 v=set()
 for r in range(len(g)):
  for c in range(len(g[0])):
   if g[r][c]==5 and (r,c) not in v:
    q=[(r,c)];b=[(r,c)];v.add((r,c))
    while q:
     y,x=q.pop()
     for Y,X in((y+1,x),(y-1,x),(y,x+1),(y,x-1)):
      try:
       if g[Y][X]==5 and (Y,X) not in v:
        v.add((Y,X));q+=[(Y,X)];b+=[(Y,X)]
      except:0
    t=min(y for y,x in b);a=min(x for y,x in b);B=max(x for y,x in b)
    for x in range(a,B+1):
     if g[t-1][x]:
      m=g[t-1][x];break
    for y,x in b: g[y][x]=m
 return g
