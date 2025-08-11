def p(g):
 v={}
 R,C=len(g),len(g[0])
 for y in range(R):
  for x in range(C):
   v.setdefault(g[y][x],set()).add((y,x))
 v.pop(0)
 items=sorted(v.items(),key=lambda i:len(i[1]))
 t,c=items[0][0],items[-1][0]
 P,Q=v[c],v[t]
 def bb(s):
  ys=[y for y,x in s]; xs=[x for y,x in s]
  return min(ys),min(xs),max(ys),max(xs)
 y0,x0,y1,x1=bb(P); h1,y1_,w1,x1_=y1-y0+1,x1-x0+1,0,0
 y2,x2,y3,x3=bb(Q); h2=y3-y2+1; w2=x3-x2+1
 M=[[1 if(y0+i,x0+j) in P else 0 for j in range(w1)]for i in range(h1)]
 T=[[1 if(y2+i,x2+j) in Q else 0 for j in range(w2)]for i in range(h2)]
 H,W=h1*h2,w1*w2
 U=[[0]*W for _ in range(H)]
 for i in range(h1):
  for j in range(w1):
   if M[i][j]:
    for a in range(h2):
     for b in range(w2):
      if T[a][b]:U[i*h2+a][j*w2+b]=t
 for dy,dx in ((0,1),(1,0),(0,-1),(-1,0)):
  sy=(y0 if dy>=0 else y0-H)+(dy>0)*(h1)+dy-1
  sx=(x1+1 if dx>0 else x0-W)+(dx<0)*0
  if 0<=sy<=R-H and 0<=sx<=C-W:
   ok=1
   for i in range(H):
    for j in range(W):
     if U[i][j] and g[sy+i][sx+j]:ok=0;break
    if not ok:break
   if ok:
    for i in range(H):
     for j in range(W):
      if U[i][j]:g[sy+i][sx+j]=U[i][j]
    break
 return g
