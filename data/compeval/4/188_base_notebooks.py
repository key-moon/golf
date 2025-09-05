p=lambda g,l=len:[r[:l(r)//2]for r in g]if l(g[0])%2<1and all(r[:l(r)//2]==r[l(r)//2:]for r in g)else g[:l(g)//2]
