def p(a):
 R,C=len(a),len(a[0]);t=range;q,r,j,b=[C]*10,[R]*10,[-1]*10,[-1]*10
 for y in t(R):
  for x,k in enumerate(a[y]):q[k]=min(q[k],x);r[k]=min(r[k],y);j[k]=max(j[k],x);b[k]=max(b[k],y)
 for k in t(1,10):
  if j[k]-q[k]==b[k]-r[k]==2:X,Y=q[k],r[k];break
 O=[[0]*C for _ in a];Z=[]
 for y in t(3):
  O[Y+y][X:X+3]=a[Y+y][X:X+3]
  for x in t(3):
   if a[Y+y][X+x]:Z+=[(x,y)]
 for dx,dy in[(x,y)for x in(-4,0,4)for y in(-4,0,4)if x|y]:
  if k:=next((a[Y+dy+y][X+dx+x]for y in t(3)for x in t(3)if 0<=Y+dy+y<R and 0<=X+dx+x<C and a[Y+dy+y][X+dx+x]),0):
   cx,cy=X,Y
   while-3<cx<C and-3<cy<R:
    cx+=dx;cy+=dy
    for x,y in Z:
     if 0<=cy+y<R and 0<=cx+x<C:O[cy+y][cx+x]=k
 return O