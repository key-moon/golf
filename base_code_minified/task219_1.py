def p(g):
	for(A,D)in((5,1),(10,2)):
		C=[A for A in range(A,A+5)if any(g[A][B]==8 for B in range(10))]
		if not C:continue
		E=C[-1]+D
		for B in range(10):
			if any(g[A][B]==8 for A in range(5))and all(g[A][B]!=8 for A in range(A,A+5)):g[E][B]=1
	return g