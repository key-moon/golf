def p(g):
 d={}
 for y,r in enumerate(g):
  for x,v in enumerate(r):
   if v:d.setdefault(v,[]).append((y,x))
 (a,p),(b,q)=d.items()
 if p[0][0]==p[1][0]:A=a;ry=p[0][0];B=b;cx=q[0][1]
 else:A=b;ry=q[0][0];B=a;cx=p[0][1]
 h,w=len(g),len(g[0])
 o=[[0]*w for _ in range(h)]
 for y in range(h):o[y][cx]=B
 for x in range(w):o[ry][x]=A
 o[ry][cx]=4
 return o
