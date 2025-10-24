from collections import*
def p(g):
 R,C=len(g),len(g[0]);v=set();S=[];T=0
 for i in range(R*C):
  r,c=divmod(i,C)
  if(r,c)not in v and g[r][c]:
   k=g[r][c];P={(r,c)};q=deque(P);v.add((r,c))
   while q:
    y,x=q.popleft()
    for Y,X in(y-1,x),(y+1,x),(y,x-1),(y,x+1):
     if 0<=Y<R and 0<=X<C and(Y,X)not in v and g[Y][X]==k:v.add((Y,X));q.append((Y,X));P.add((Y,X))
   S.append((k,P))
 for k,P in S:
  if k==5:
   ys,xs=zip(*P);y1,x1,y2,x2=min(ys),min(xs),max(ys),max(xs)
   if P==({(y,x)for y in(y1,y2)for x in range(x1,x2+1)}|{(y,x)for x in(x1,x2)for y in range(y1,y2+1)})and(I:={(y,x)for y in range(y1+1,y2)for x in range(x1+1,x2)if g[y][x]}):
    iys,ixs=zip(*I);T=(frozenset((y-min(iys),x-min(ixs))for y,x in I),Counter(g[y][x]for y,x in I).most_common(1)[0][0]);break
 if not T:return g
 g=[[*r]for r in g];TP,kc=T
 for k,P in S:
  ys,xs=zip(*P)
  if frozenset((y-min(ys),x-min(xs))for y,x in P)==TP:
   for y,x in P:g[y][x]=kc
 return g
