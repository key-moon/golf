def p(g):
	C=max(map(max,g))
	for(D,A)in enumerate(g):
		for(B,E)in enumerate(A):A[B]=(D+B)%C+1
	return g