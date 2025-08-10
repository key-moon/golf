f=lambda r:[r[0]]*len(r)if r[0]else r
t=lambda g:[[g[y][x]for y in range(len(g))]for x in range(len(g[0]))]
q=lambda g:[f(r)for r in g]
p=lambda g:t(q(t(g)))if q(g)==g else q(g)