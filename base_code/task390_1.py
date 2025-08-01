def p(val_g):
 val_O=[r[:]for r in val_g];h=len(val_g);w=len(val_g[0])
 S={(i,j)for i in range(h)for j in range(w)if val_g[i][j]==5}
 for i,j in S:val_g[i][j]=0
 while S:
  C={S.pop()};q=[*C]
  while q:
   i,j=q.pop()
   for di,dj in((1,0),(-1,0),(0,1),(0,-1)):
    x,y=i+di,j+dj
    if(x,y)in S:S.remove((x,y));C.add((x,y));q.append((x,y))
  B={(i+di,j+dj)for i,j in C for di,dj in((1,0),(-1,0),(0,1),(0,-1))
      if 0<=i+di<h and 0<=j+dj<w and val_O[i+di][j+dj]==2}
  rs={i for i,j in B};cs={j for i,j in B}
  if len(rs)==1:a,l=0,rs.pop()
  else:a,l=1,cs.pop()
  for i,j in C:
   if a:val_g[i][2*l-j]=5
   else:val_g[2*l-i][j]=5
 return val_g
