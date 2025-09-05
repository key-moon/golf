def p(g):
 R=range
 for a in R(3):
  for b in R(3):
   if sum(g[a*4+r][b*4+c]==0for r in R(3)for c in R(3))==5:
    s=[[5if i%4==3or j%4==3else 0for j in R(11)]for i in R(11)]
    for r in R(3):
     for c in R(3):
      v=g[a*4+r][b*4+c]
      if v:
       for x in R(3):
        for y in R(3):s[r*4+x][c*4+y]=v
    return s