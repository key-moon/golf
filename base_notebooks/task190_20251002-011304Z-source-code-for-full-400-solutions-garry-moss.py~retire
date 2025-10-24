def p(i):
 c=range;o=[d[:]for d in i];h=[(0,1),(1,0),(0,-1),(-1,0)];p=[(-1,-1),(-1,1),(1,1),(1,-1)]
 for d in c(10):
  for u in c(10):
   if i[d][u]and all(0<=d+b<10and 0<=u+c<10and i[d+b][u+c]==0for(b,c)in h):
    for b in p:
     f,n=d+b[0],u+b[1]
     if 0<=f<10and 0<=n<10and i[f][n]:
      l,b=-b[0],-b[1]
      for r in c(1,10):
       f,n=d+l*r,u+b*r
       if 0<=f<10and 0<=n<10:o[f][n]=i[d][u]
 return o