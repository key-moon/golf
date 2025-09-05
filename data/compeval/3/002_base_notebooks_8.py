def p(g):
 h,w,i=len(g),len(g[0]),0
 for r,c in(q:=[(r,c)for r in range(h)for c in range(w)if g[r][c]==0 and(r*c==0 or r==h-1 or c==w-1)]):g[r][c]=1
 while i<len(q):
  r,c=q[i];i+=1
  for y,x in(r+1,c),(r-1,c),(r,c+1),(r,c-1):
   if 0<=y<h and 0<=x<w and g[y][x]==0:g[y][x]=1;q.append((y,x))
 return[[{0:4,1:0}.get(x,x)for x in r]for r in g]