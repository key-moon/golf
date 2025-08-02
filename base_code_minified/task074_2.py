def p(g):
	D=max(map(max,g));C=len(g)
	for A in range(C):
		for B in range(C):
			if g[A][B]==D:g[A][B]=g[B][A]
	return g