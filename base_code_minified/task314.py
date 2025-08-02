def p(g):
	D=range(8)
	for A in D:
		for B in D:
			for C in D[B+1:]:
				if g[A][B]==g[A][C]!=0 and not B+C&1:g[A][B+C>>1]=g[A][B]
	for A in D:
		for B in D:
			for C in D[A+1:]:
				if g[A][B]==g[C][B]!=0 and not A+C&1:g[A+C>>1][B]=g[A][B]
	return g