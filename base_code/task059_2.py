def p(g):
 r=(0,4,8)
 for bi in range(3):
  for bj in range(3):
   i0,j0=r[bi],r[bj]
   col=None;rows=set()
   for i in range(i0,i0+3):
    for j in range(j0,j0+3):
     v=g[i][j]
     if v and v!=5:
      col=v;rows.add(i)
   if col and len(rows)>1:
    for i in range(i0,i0+3):
     for j in range(j0,j0+3):
      g[i][j]=col
 return g
