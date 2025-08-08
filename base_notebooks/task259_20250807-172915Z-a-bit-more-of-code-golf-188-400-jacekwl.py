def p(g,R=range):
 w,h=len(g),len(g[0]);a,b,c,d=w,0,h,0
 for i in R(w):
  for j in R(h):
   if g[i][j]-1:
    if i<a:a=i
    if i>b:b=i
    if j<c:c=j
    if j>d:d=j
 return[[x-(x==1)for x in r[c:d+1]]for r in g[a:b+1]]