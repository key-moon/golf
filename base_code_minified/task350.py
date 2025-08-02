def p(g):
	for(C,D)in enumerate(g):
		A=[A for(A,B)in enumerate(D)if B==1]
		if A:
			for B in range(A[0]+1,A[-1]):D[B]=8
	for B in range(len(g[0])):
		A=[A for A in range(len(g))if g[A][B]==1]
		if A:
			for C in range(A[0]+1,A[-1]):g[C][B]=8
	return g