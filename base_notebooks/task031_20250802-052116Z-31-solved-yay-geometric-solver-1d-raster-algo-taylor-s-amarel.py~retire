def p(g):
 rows,cols=[],[]
 for i in range(len(g)):
  for j in range(len(g[0])):
   if g[i][j]>0:
    rows.append(i)
    cols.append(j)
 if not rows:return g
 r0,r1=min(rows),max(rows)+1
 c0,c1=min(cols),max(cols)+1
 return[r[c0:c1]for r in g[r0:r1]]
