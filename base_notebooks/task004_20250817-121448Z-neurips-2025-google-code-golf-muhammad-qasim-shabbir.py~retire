def p(g):
 s={}
 E=enumerate
 for r,R in E(g):
  for c,C in E(R):
   if C:s.setdefault(C,[]).append((r,c))
 o=[[0]*len(g[0])for _ in g]
 for C,P in s.items():
  F,N=max(r for r,_ in P),max(c for _,c in P)
  for r,c in P:o[r][c if r==F or c==N else c+1]=C
 return o