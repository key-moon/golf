def p(g):
	C=len(g)
	for A in range(C):
		for B in range(C):
			if g[A][B]==1:
				if A:g[A-1][B]=2
				if B:g[A][B-1]=7
				if A+1<C:g[A+1][B]=8
				if B+1<C:g[A][B+1]=6
	return g