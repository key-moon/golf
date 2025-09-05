def p(g):
 q=range
 n=len(g)
 r=[[0]*n for _ in q(n)]
 x,y=0,0
 dirs=[(0,1),(1,0),(0,-1),(-1,0)]
 for i in q(n):
  r[x][y]=3
  if i<n-1:y+=1
 m=n-1
 d=1
 while m>0:
  for _ in q(2):
   if m>0:
    x,y=x+dirs[d][0],y+dirs[d][1]
    for i in q(m):
     r[x][y]=3
     if i<m-1:x,y=x+dirs[d][0],y+dirs[d][1]
    d=(d+1)%4
  m-=2
 return r