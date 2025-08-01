def p(g):
 u=[r[:]for r in g]
 # find colors A(count=1),B(count=4),C(count>4)
 d={}
 for y,r in enumerate(g):
  for x,v in enumerate(r):d[v]=d.get(v,[])+[(y,x)]
 A,B,C=[c for c in d if len(d[c]) in(1,4)][0],\
       [c for c in d if len(d[c])==4 and c!=[c for c in d if len(d)==1][0]][0],\
       [c for c in d if len(d[c])>4][0]
 # center of arrow
 ay,ax=d[A][0]
 # arms of B on same row → direction D
 D=next((0, x-ax) for y,x in d[B] if y==ay and x!=ax)
 D=(0,D)
 P=(-D[1],D[0])
 # bounding rect of C
 ys=[y for y,x in d[C]]; xs=[x for y,x in d[C]]
 my,MY=min(ys),max(ys); mx,MX=min(xs),max(xs)
 H=MY-my+1; W=MX-mx+1
 # stamp at i*D for i=0…W-1 and at ±H*P (i=0 only)
 for i in list(range(W))+[-H,H]:
  if i and abs(i)!=H:continue
  dy,dx=(D[0]*i+P[0]*(i//abs(i) if abs(i)==H else 0),
        D[1]*i+P[1]*(i//abs(i) if abs(i)==H else 0))
  for y in range(my,MY+1):
   for x in range(mx,MX+1):
    if g[y][x]==C:u[y+dy][x+dx]=C
 return u
