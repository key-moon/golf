def p(m,u=range):
 r,c,n=len(m),len(m[0]),0
 v=[[0]*c for _ in m]
 def d(y,x):
  s=[(y,x)]
  v[y][x]=1
  while s:
   y,x=s.pop()
   for R,T in[(-1,0),(1,0),(0,-1),(0,1)]:
    Q,e=y+R,x+T
    if 0<=Q<r and 0<=e<c and m[Q][e]and not v[Q][e]:v[Q][e]=1;s+=[(Q,e)]
 for y in u(r):
  for x in u(c):
   if m[y][x]and not v[y][x]:n+=1;d(y,x)
 return[[8*(i==j)for j in u(n)]for i in u(n)]