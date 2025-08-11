def p(g):
 h,w=len(g),len(g[0])
 c=[[0]*w for _ in range(h)]
 cid=1
 v=set()
 for i in range(h):
  for j in range(w):
   if g[i][j]!=0 and(i,j)not in v:
    q=[(i,j)]
    comp=[]
    while q:
     y,x=q.pop(0)
     if(y,x)in v:continue
     v.add((y,x))
     comp.append((y,x))
     for dy,dx in[(0,1),(1,0),(0,-1),(-1,0)]:
      ny,nx=y+dy,x+dx
      if 0<=ny<h and 0<=nx<w and g[ny][nx]!=0 and(ny,nx)not in v:
       q.append((ny,nx))
    for y,x in comp:
     c[y][x]=cid
    cid=(cid%9)+1
 return c
