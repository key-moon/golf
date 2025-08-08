def p(m,K=range):
 r,c=len(m),len(m[0]);n=0
 def f(y,x):
  m[y][x]=0
  for b,a in(1,0),(-1,0),(0,1),(0,-1):
   Y,X=y+b,x+a
   if 0<=Y<r and 0<=X<c and m[Y][X]:f(Y,X)
 for i in K(r):
  for j in K(c):
   if m[i][j]:n+=1;f(i,j)
 return[[8*(i==j)for j in K(n)]for i in K(n)]