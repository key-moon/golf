def p(m):
 a,b=len(m),len(m[0]);v=[[0]*b for _ in m];r=[]
 def f(i,j):
  q=[(i,j)];v[i][j]=1;c=[(i,j)];d=1
  while q:
   x,y=q.pop()
   for u,O in[(0,1),(1,0),(0,-1),(-1,0)]:
    p,S=x+u,y+O
    if not(0<=p<a and 0<=S<b):d=0;continue
    if m[p][S]<1 and not v[p][S]:v[p][S]=1;q+=[(p,S)];c+=[(p,S)]
  return c if d else[]
 for i in range(a):
  for j in range(b-1,-1,-1):
   if m[i][j]<1 and not v[i][j]:r+=[f(i,j)]
 r.sort(key=len,reverse=1)
 for i,x in enumerate(r):
  t=min(8,max(6,len(x)**.5+.5//1+5))
  for y in x:m[y[0]][y[1]]=t
 return m