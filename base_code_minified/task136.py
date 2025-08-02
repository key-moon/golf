def p(g):
	E,F=len(g),len(g[0])
	for B in(1,2):
		C=min(A for(A,C)in enumerate(g)for D in C if D==B);D=min(C for A in g for(C,D)in enumerate(A)if D==B)
		for A in range(10):
			if C-A>=0 and D-A>=0:g[C-A][D-A]=B
			if C+1+A<E and D+1+A<F:g[C+1+A][D+1+A]=B
	return g