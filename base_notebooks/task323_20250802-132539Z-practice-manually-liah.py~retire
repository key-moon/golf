def p(m):
 r,c=len(m),len(m[0])
 o=[i[:]for i in m]
 i,j=[(i,j)for i in range(r)for j in range(c)if m[i][j]][0]
 for a,b in(((-1,1),(2,2)),((1,-1),(2,2))):
  x,y=i,j
  while 1:
   for _ in[0]*b[0]:
    x+=a[0]
    if 0<=x<r:o[x][y]=5
    else:break
   else:
    for _ in[0]*b[1]:
     y+=a[1]
     if 0<=y<c:o[x][y]=5
     else:break
    else:continue
   break
 return o
