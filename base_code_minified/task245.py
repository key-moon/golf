def p(g):
	C=len(g);E=0;D=len(g[0]);F=0
	for(A,G)in enumerate(g):
		for(B,H)in enumerate(G):
			if H==3:C=min(C,A);E=max(E,A);D=min(D,B);F=max(F,B)
	I=[A[D:F+1]for A in g[C:E+1]];J=zip(*I[::-1])
	for A in range(C,E+1):
		for B in range(D,F+1):
			if g[A][B]^3:g[A][B]=J[A-C][B-D]
	return g