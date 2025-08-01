def p(g):
 h,w=len(g),len(g[0])
 v=set()
 for i in range(h):
  for j in range(w):
   if g[i][j]==4 and (i,j) not in v:
    s=[(i,j)];v.add((i,j))
    r0=r1=i;c0=c1=j
    while s:
     x,y=s.pop()
     if x<r0:r0=x
     if x>r1:r1=x
     if y<c0:c0=y
     if y>c1:c1=y
     for a,b in((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
      if 0<=a<h and 0<=b<w and g[a][b]==4 and (a,b) not in v:
       v.add((a,b));s.append((a,b))
    for a in range(r0,r1+1):
     for b in range(c0,c1+1):
      if g[a][b]==0:g[a][b]=7
 return g
