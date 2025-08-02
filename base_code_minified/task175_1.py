def p(g):
	C,D=len(g),len(g[0])
	for A in range(C):
		for B in range(D):
			if g[A][B]==0:g[A][B]=g[A][B-1]or g[A][B+1]or g[A-1][B]or g[A+1][B]
	return g