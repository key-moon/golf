def p(g):
	F=[A[:]for A in g];G,H=len(g),len(g[0])
	for B in range(G):
		for C in range(H):
			if g[B][C]:
				I=g[B][C]
				for A in[(-1,-1),(-1,1),(1,1),(1,-1)]:
					D,E=B+A[0],C+A[1]
					while 0<=D<G and 0<=E<H:F[D][E]=I;D+=A[0];E+=A[1]
	return F