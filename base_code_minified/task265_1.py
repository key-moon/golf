def p(g):
	for A in range(len(g)-1):
		for B in range(len(g[0])-1):
			if not g[A][B]and not g[A][B+1]and not g[A+1][B]and not g[A+1][B+1]:g[A][B]=g[A][B+1]=g[A+1][B]=g[A+1][B+1]=2
	return g