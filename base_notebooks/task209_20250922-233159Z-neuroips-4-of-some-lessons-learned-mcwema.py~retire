from itertools import product as P, groupby as G
def p(f):
 R,C=len(f),len(f[0])
 s=sorted((y,x)for y,x in P(range(R),range(C))if f[y][x]==4)
 if len(s)!=4:return[]
 y1,x1,y2,x2=s[0]+s[3]
 A=[(y,x)for y,x in P(range(R),range(C))if f[y][x]and not(y1<=y<=y2 and x1<=x<=x2)]
 if not A:return[[4 if(y,x)in((0,0),(0,x2-x1),(y2-y1,0),(y2-y1,x2-x1))else 0 for x in range(x2-x1+1)]for y in range(y2-y1+1)]
 mr,mc=min(y for y,_ in A),min(x for _,x in A)
 B=[(y,x)for y in range(y1,y2+1)for x in range(x1,x2+1)if f[y][x]not in(0,4)]
 if not B:
  q=[[0]*(x2-x1+1)for _ in range(y2-y1+1)]
  q[0][0]=q[0][-1]=q[-1][0]=q[-1][-1]=4
  return q
 def d(f,y1,y2,x1,x2):
  D=float('inf')
  for i in range(y1,y2+1):
   a=[f[i][j]for j in range(x1,x2+1)if f[i][j]not in(0,4)]
   if a:D=min(D,max(sum(1for _ in g)for _,g in G(a)))
  for j in range(x1,x2+1):
   a=[f[i][j]for i in range(y1,y2+1)if f[i][j]not in(0,4)]
   if a:D=min(D,max(sum(1for _ in g)for _,g in G(a)))
  return D if D!=float('inf')else 1
 D=d(f,y1,y2,x1,x2)
 M={}
 for y,x in B:
  n=f[y][x]
  if n not in M:M[n]=[[f[y+i][x+j]for j in range(D)]for i in range(D)]
 fb=B[0];fn=f[fb[0]][fb[1]]
 fa=next(((y-mr,x-mc)for y,x in A if f[y][x]==fn),(-1,-1))
 def b(yo,xo):
  q=[[0]*(x2-x1+1)for _ in range(y2-y1+1)]
  q[0][0]=q[0][-1]=q[-1][0]=q[-1][-1]=4
  for y,x in A:
   m=M.get(f[y][x],[[f[y][x]]*D]*D)
   sy,sx=yo+(y-mr)*D,xo+(x-mc)*D
   for dy,dx in P(range(D),repeat=2):
    ny,nx=sy+dy,sx+dx
    if 0<=ny<len(q)and 0<=nx<len(q[0]):q[ny][nx]=m[dy][dx]
  return q
 yo=(fb[0]-y1)-fa[0]*D if fa!=(-1,-1)else 0
 xo=(fb[1]-x1)-fa[1]*D if fa!=(-1,-1)else 0
 q=b(yo,xo)
 if any(f[y][x]not in(0,4)and not q[y-y1][x-x1]for y,x in P(range(y1,y2+1),range(x1,x2+1))):
  rb,cb,nb=next((y,x,f[y][x])for y in range(y2,y1-1,-1)for x in range(x1,x2+1)if f[y][x]not in(0,4))
  T=[(y,x)for y,x in A if f[y][x]==nb]
  my,mx=max(y for y,_ in T),min(x for _,x in T)
  yo=(rb-y1)-((my-mr)*D+D-1)
  xo=(cb-x1)-(mx-mc)*D
  q=b(yo,xo)
 return q