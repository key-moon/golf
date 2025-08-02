def p(g):
	A=g[-1][0];B=min(A for B in g for A in B if A)
	for(C,D)in enumerate(g):
		for(E,F)in enumerate(D):
			if F==B:g[C][E]=A
	g[-1][0]=0;return g