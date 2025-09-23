def p(g):
 s=len(g);b=[(r,c)for r in range(s)for c in range(s)if g[r][c]==0]
 if not b:return[[]]
 R,C=min(r for r,c in b),min(c for r,c in b);H,W=max(r for r,c in b)-R+1,max(c for r,c in b)-C+1
 for m in range(2,5):
  c,v=[],1
  for r in range(m):
   for k in range(m):
    x=None
    for i in range(r,s,m):
     for j in range(k,s,m):
      if g[i][j]!=0:
       if x is None:x=g[i][j]
       elif x!=g[i][j]:v=0;break
     if not v:break
    if not v or x is None:v=0;break
    c.append(x)
   if not v:break
  if v and len(c)==m*m:
   if all(g[r][k]==0 or g[r][k]==c[r%m*m+k%m]for r in range(s)for k in range(s)):
    return[[c[(R+r)%m*m+(C+k)%m]for k in range(W)]for r in range(H)]
 return[[]]
