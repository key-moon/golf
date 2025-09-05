def p(m,D=range):
 r,c,n=len(m),len(m[0]),0
 v=[[0]*c for _ in m]
 def d(y,x):
  s=[(y,x)]
  v[y][x]=1
  while s:
   y,x=s.pop()
   for b,g in[(-1,0),(1,0),(0,-1),(0,1)]:
    E,L=y+b,x+g
    if 0<=E<r and 0<=L<c and m[E][L]and not v[E][L]:v[E][L]=1;s+=[(E,L)]
 for y in D(r):
  for x in D(c):
   if m[y][x]and not v[y][x]:n+=1;d(y,x)
 return[[8*(i==j)for j in D(n)]for i in D(n)]