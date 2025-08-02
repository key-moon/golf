def p(g):
	E=len(g);C=0
	for(A,G)in enumerate(g):
		for(B,H)in enumerate(G):
			if H and A+B+1>C:C=A+B+1
	D=E*C;F=[[0]*D for A in range(D)]
	for A in range(D):
		I,J=divmod(A,E)
		for B in range(D):
			K,L=divmod(B,E)
			if I+K<C:F[A][B]=g[J][L]
	return F