def p(g):
	B=g[0];C=[(A,B)for(B,A)in enumerate(B)if A];A=len(B)*len(C);g=[[0]*A for B in range(A)]
	for D in range(A):
		for(F,G)in C:
			E=G+D
			if E<A:g[A-1-D][E]=F
	return g