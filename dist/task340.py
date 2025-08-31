def p(g):
 for _ in range(4):g=[[s[0],max({*s[:2]}&{*s[2:]}),*s[2:]]for s in zip(*g[::-1])]
 return g[:2]+[s[:2]+[0]*(len(s)-4)+s[-2:]for s in g[2:-2]]+g[-2:]