from collections import*
def p(a):
 if not a or not a[0]:return[]
 r,c=len(a),len(a[0])
 q=deque([(i,j)for i in range(r)for j in range(c)if(i*j==0 or i==r-1 or j==c-1)and a[i][j]==0])
 while q:
  x,y=q.popleft();a[x][y]=1
  for dx,dy in[(0,1),(0,-1),(1,0),(-1,0)]:
   nx,ny=x+dx,y+dy
   if 0<=nx<r and 0<=ny<c and a[nx][ny]==0:q.append((nx,ny));a[nx][ny]=1
 return[[4 if v==0 else 0 if v==1 else v for v in row]for row in a]
