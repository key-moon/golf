def p(g):
 h,w=len(g),len(g[0])
 q=[(r,c)for r in range(h)for c in range(w)if not g[r][c]and r*(h-1-r)*c*(w-1-c)==0]
 for r,c in q:g[r][c]=1
 i=0
 while i<len(q):
  r,c=q[i];i+=1
  for Y,X in((1,0),(-1,0),(0,1),(0,-1)):
   y,x=r+Y,c+X
   if 0<=y<h and 0<=x<w and not g[y][x]:g[y][x]=1;q+=[(y,x)]
 return[[x*(x>1)+4*(x<1)for x in u]for u in g]