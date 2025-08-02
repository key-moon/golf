def p(g):
	D=len(g);E=max(map(max,g))
	for(F,C)in enumerate(g):
		for(B,G)in enumerate(C):
			if not G:
				A=F
				while not g[A][B]:A=(A+E)%D
				C[B]=g[A][B]
	return g