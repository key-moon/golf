D=range
B=len
E=lambda r:[r[0]]*B(r)if r[0]else r
C=lambda g:[[g[y][x]for y in D(B(g))]for x in D(B(g[0]))]
A=lambda g:[E(r)for r in g]
p=lambda g:C(A(C(g)))if A(g)==g else A(g)