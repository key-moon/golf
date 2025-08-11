def p(g):
 a=sum(g,[]);v=set(a)-{0}
 c=max(v,key=a.count)
 h,w=len(g),len(g[0])
 m=[ [c if g[y][x]==c else -1 for x in range(w)] for y in range(h) ]
 s=[(y,x) for x in range(w) for y in(0,h-1) if m[y][x]==-1]+[(y,x) for y in range(h) for x in(0,w-1) if m[y][x]==-1]
 while s:
  y,x=s.pop();m[y][x]=-2
  for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
   ny, nx=y+dy, x+dx
   if 0<=ny<h and 0<=nx<w and m[ny][nx]==-1: s.append((ny,nx))
 for y in range(h):
  for x in range(w):
   if m[y][x]==-1: m[y][x]=c
   elif m[y][x]==-2: m[y][x]=0
 return m
