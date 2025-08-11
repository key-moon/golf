def p(m):
 r,c,n=len(m),len(m[0]),0
 v=[[0]*c for _ in m]
 def d(y,x):
  s=[(y,x)]
  v[y][x]=1
  while s:
   y,x=s.pop()
   for dy,dx in[(-1,0),(1,0),(0,-1),(0,1)]:
    ny,nx=y+dy,x+dx
    if 0<=ny<r and 0<=nx<c and m[ny][nx]and not v[ny][nx]:
     v[ny][nx]=1
     s+=[(ny,nx)]
 for y in range(r):
  for x in range(c):
   if m[y][x]and not v[y][x]:
    n+=1;d(y,x)
 return[[8*(i==j)for j in range(n)]for i in range(n)]
