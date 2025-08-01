def p(g):
 x=min(i for i,row in enumerate(g) for j,v in enumerate(row) if v==8)
 y=max(i for i,row in enumerate(g) for j,v in enumerate(row) if v==8)
 z=min(j for row in g for j,v in enumerate(row) if v==8)
 w=max(j for row in g for j,v in enumerate(row) if v==8)
 for i,row in enumerate(g):
  for j,v in enumerate(row):
   if v and v!=8:
    if j<z: row[z]=v
    elif j>w: row[w]=v
    elif i<x: g[x][j]=v
    else:    g[y][j]=v
 return g
