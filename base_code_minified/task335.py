def p(g):
	for(A,J)in enumerate(g):
		for(B,H)in enumerate(J):
			if H==8:C,E=B,A
			if H==2:F,D=B,A
	G=(D>E)-(D<E)
	for A in range(E+G,D+G,G):g[A][C]=4
	I=(F>C)-(F<C)
	for B in range(C+I,F,I):g[D][B]=4
	return g