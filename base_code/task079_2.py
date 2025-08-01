def p(g):
 v = max({c for r in g for c in r if c}, key=lambda c: sum(rr.count(c) for rr in g))
 t = sum(r.count(v) for r in g) // 3
 H, W = len(g), len(g[0])
 for i in range(H-2):
  for j in range(W-2):
   s = sum(g[i+a][j+b]==v for a in (0,1,2) for b in (0,1,2))
   if s==t and all(g[i+a][j+b] in (0,v) for a in (0,1,2) for b in (0,1,2)):
    return [row[j:j+3] for row in g[i:i+3]]
