def p(g):
 H=len(g);W=len(g[0])
 if H%3 or W%3:return g
 o=[]
 for i in range(0,H,3):
  r=[]
  for j in range(0,W,3):
   b=[g[i+a][j+b]for a in(0,1,2)for b in(0,1,2)]
   r.append(max(b,key=b.count))
  o.append(r)
 return o