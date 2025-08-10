def p(g):
 res=[r[:]for r in g]
 for c in range(1,10):
  pos=[(i,j)for i in range(len(g))for j in range(len(g[0]))if g[i][j]==c]
  for i in range(len(pos)):
   for j in range(i+1,len(pos)):
    y1,x1=pos[i]
    y2,x2=pos[j]
    if y1==y2:
     for x in range(min(x1,x2),max(x1,x2)+1):
      res[y1][x]=8
    elif x1==x2:
     for y in range(min(y1,y2),max(y1,y2)+1):
      res[y][x1]=8
  for y1,y2 in pos:
   res[y1][y2]=1
 return res
