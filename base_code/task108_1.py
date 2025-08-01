def p(g):
 b=len(g)*2//5;h=[[0]*b*5 for _ in[0]*b*5]
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v:
    x=i//2*b;y=j//2*b
    for k in range(b):h[x+k][y:y+b]=[v]*b
 return h
