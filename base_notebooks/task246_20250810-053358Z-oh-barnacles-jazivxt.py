def p(g):
 q=range
 r=[x[:]for x in g]
 for i in q(len(g)):
  for j in q(len(g[0])):
   if g[i][j]==2:a,b=i,j
   if g[i][j]==3:x,y=i,j
 d=1if y>b else-1
 for j in q(b+d,y+d,d):r[a][j]=8
 d=1if x>a else-1
 for i in q(a+d,x,d):r[i][y]=8
 return r
