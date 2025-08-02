def p(g):
	C=len(g)
	for A in range(C):
		for B in range(C):
			if g[A][B]!=5:g[A][B]=g[A//4*4][B//4*4]
	return g