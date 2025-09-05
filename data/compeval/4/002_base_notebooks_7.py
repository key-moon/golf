from collections import*
def p(a):
 if not a or not a[0]:return[]
 r,c=len(a),len(a[0])
 q=deque([(i,j)for i in range(r)for j in range(c)if(i*j==0 or i==r-1 or j==c-1)and a[i][j]==0])
 while q:
  x,y=q.popleft();a[x][y]=1
  for Q,R in[(0,1),(0,-1),(1,0),(-1,0)]:
   s,u=x+Q,y+R
   if 0<=s<r and 0<=u<c and a[s][u]==0:q.append((s,u));a[s][u]=1
 return[[4 if v==0 else 0 if v==1 else v for v in T]for T in a]