def p(g):
	F=len(g)
	for D in g:
		A=[A for(A,B)in enumerate(D)if B==1]
		for(B,C)in zip(A,A[1:]):
			for G in range(B+1,C):D[G]=8
	for E in range(len(g[0])):
		A=[A for A in range(F)if g[A][E]==1]
		for(B,C)in zip(A,A[1:]):
			for H in range(B+1,C):g[H][E]=8
	return g