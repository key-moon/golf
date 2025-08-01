def p(g):
 H,W=len(g),len(g[0])
 C={c for R in g for c in R}-{0}
 for c in C:
  P=[(i,j)for i,R in enumerate(g)for j,v in enumerate(R)if v==c]
  ys=[i for i,_ in P]; xs=[j for _,j in P]
  y0,y1,min(xs),x1=min(ys),max(ys);x0,x1=min(xs),max(xs)
  h,y0=h,y0=y1-y0+1,y0;w,x0=w,x0=x1-x0+1
  if h>w:
    for dx in range(w+1,W-x0,w+1):
      for i,j in P:g[i][j+dx]=c
  elif w>h:
    for dy in range(h+1,H-y0,h+1):
      for i,j in P:g[i+dy][j]=c
 return g
