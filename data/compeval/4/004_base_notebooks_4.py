def p(g):
  s={}
  E=enumerate
  for r,R in E(g):
    for c,C in E(R):
      if C:s.setdefault(C,[]).append((r,c))
  o=[[0]*len(g[0])for _ in g]
  for C,P in s.items():
    mr,mc=max(r for r,_ in P),max(c for _,c in P)
    for r,c in P:o[r][c if r==mr or c==mc else c+1]=C
  return o
