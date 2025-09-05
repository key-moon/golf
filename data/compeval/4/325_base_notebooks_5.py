def p(m,k=range):
 r,c,n=len(m),len(m[0]),0
 v=[[0]*c for _ in m]
 def d(y,x):
  s=[(y,x)]
  v[y][x]=1
  while s:
   y,x=s.pop()
   for g,D in[(-1,0),(1,0),(0,-1),(0,1)]:
    K,X=y+g,x+D
    if 0<=K<r and 0<=X<c and m[K][X]and not v[K][X]:v[K][X]=1;s+=[(K,X)]
 for y in k(r):
  for x in k(c):
   if m[y][x]and not v[y][x]:n+=1;d(y,x)
 return[[8*(i==j)for j in k(n)]for i in k(n)]