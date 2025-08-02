def p(g):
	A=len(g)//2;C=2*A;H=g[A][A];B=[[0]*C for A in[0]*C]
	for D in range(A):
		for E in range(A):
			if g[D][E]:F=C-1-D;G=C-1-E;B[D][E]=B[D][G]=B[F][E]=B[F][G]=H
	return B