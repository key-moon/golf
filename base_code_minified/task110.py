def p(g):
	C=len(g)
	for D in range(C):
		for E in range(C):
			if not g[D][E]:
				A,B=D,E
				for F in range(3):
					A,B=B,C-1-A
					if g[A][B]:g[D][E]=g[A][B];break
	return g