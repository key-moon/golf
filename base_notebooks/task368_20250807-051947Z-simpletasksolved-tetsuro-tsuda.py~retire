def p(g):
 R=range
 b=[]
 for i in R(10):
  for j in R(10):
   if g[i][j]and(i<1or not g[i-1][j])and(j<1or not g[i][j-1]):
    h=w=1
    while i+h<10and g[i+h][j]:h+=1
    while j+w<10and g[i][j+w]:w+=1
    b.append((i,j,[[g[i+r][j+s]for s in R(w)]for r in R(h)]))
 t=next(k for _,_,k in b if any(k[r][s]!=5 for r in R(len(k))for s in R(len(k[0]))))
 r=[x[:]for x in g]
 for x,y,k in b:
  if all(k[r][s]==5 for r in R(len(k))for s in R(len(k[0]))):
   for u in R(len(k)):
    for v in R(len(k[0])):r[x+u][y+v]=t[u][v]
 return r