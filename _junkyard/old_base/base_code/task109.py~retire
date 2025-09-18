def p(g):
 for r,rw in enumerate(g):
  if len({*rw})==1 and rw[0]:d=rw[0];break
 c=next(j for j in range(len(g[0]))if all(g[i][j]==d for i in range(len(g))))
 a=[x[:c]for x in g[:r]];h=len(a);w=len(a[0])
 o=[[0]*(2*w)for _ in range(2*h)]
 for i in range(h):
  for j in range(w):
   if a[i][j]:
    o[i][j]=o[i][2*w-1-j]=o[2*h-1-i][j]=o[2*h-1-i][2*w-1-j]=d
 return o
