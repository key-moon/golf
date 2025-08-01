def p(g):
 m = sum(v>0 for r in g for v in r)
 return [sum([[c]*m for c in r], []) for r in g for _ in [0]*m]