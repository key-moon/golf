def p(m):
 a,b=len(m),len(m[0]);v=[[0]*b for _ in m];r=[]
 def f(i,j):
  q=[(i,j)];v[i][j]=1;c=[(i,j)];d=1
  while q:
   x,y=q.pop()
   for u,vv in[(0,1),(1,0),(0,-1),(-1,0)]:
    nx,ny=x+u,y+vv
    if not(0<=nx<a and 0<=ny<b):d=0;continue
    if m[nx][ny]<1 and not v[nx][ny]:v[nx][ny]=1;q+=[(nx,ny)];c+=[(nx,ny)]
  return c if d else[]
 for i in range(a):
  for j in range(b-1,-1,-1):
   if m[i][j]<1 and not v[i][j]:r+=[f(i,j)]
 r.sort(key=len,reverse=1)
 for i,x in enumerate(r):
  t=min(8,max(6,len(x)**.5+.5//1+5))
  for y in x:m[y[0]][y[1]]=t
 return m
