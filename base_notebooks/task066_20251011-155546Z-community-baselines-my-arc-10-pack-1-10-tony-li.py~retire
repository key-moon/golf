def p(g):
 h,w=len(g),len(g[0]);o=[r[:]for r in g];f=lambda v:[(y,x)for y in range(h)for x in range(w)if g[y][x]==v];S,T=f(3),f(2)
 if len(S)<2 or len(T)<2:return o
 s,t=[(sum(c[0]for c in L)/2,sum(c[1]for c in L)/2)for L in[S,T]];hs=S[0][0]==S[1][0];P=B=None;sT=set(T)
 for d in [(0,-1),(0,1)]if hs else[(-1,0),(1,0)]:
  p=set();c=(min,max)[d[0]+d[1]>0](S,key=lambda i:i[hs]);y,x=c;dy,dx=d
  while 0<=y+dy<h and 0<=x+dx<w and g[y+dy][x+dx]!=8:y+=dy;x+=dx;p.add((y,x))
  dy,dx=[(0,(1,-1)[t[1]<=s[1]]),((1,-1)[t[0]<=s[0]],0)][hs]
  while 0<=y+dy<h and 0<=x+dx<w and g[y+dy][x+dx]!=8:y+=dy;x+=dx;p.add((y,x))
  dy,dx=[(((1,-1)[t[0]<=y]),0),(0,(1,-1)[t[1]<=x])][hs]
  while 0<=y+dy<h and 0<=x+dx<w and g[y+dy][x+dx]!=8:
   y+=dy;x+=dx;p.add((y,x))
   if(y,x)in sT:break
  if not p&sT:continue
  oy,ox=c[0]+d[0],c[1]+d[1];W=0
  if 0<=oy<h and 0<=ox<w:
   if g[oy][ox]==8:W=1
   else:
    wy,wx=oy,ox
    while 0<=wy<h and 0<=wx<w:
     if g[wy][wx]==8:break
     wy+=d[0];wx+=d[1]
    else:W=1
  if not W:P=p;break
  if B is None:B=p
 if P:=P or B:
  for y,x in P:
   if o[y][x]==0:o[y][x]=3
 return o
