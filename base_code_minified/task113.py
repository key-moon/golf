def p(g):
	A=0
	while any(g[A]):A+=1
	for B in range(A):g[-B-1]=g[B]
	return g