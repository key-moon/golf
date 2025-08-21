def p(g):
 h=len(g);w=len(g[0]);t=[[v>0 for v in r]for r in g]
 o=[[0]*(w*h)for _ in range(h*h)]
 for i,r in enumerate(g):
  for j,c in enumerate(r):
   if c:
    bi=i*h;bj=j*w
    for a in range(h):
     tr=t[a];d=o[bi+a]
     for b in range(w):
      if tr[b]:d[bj+b]=c
 return o