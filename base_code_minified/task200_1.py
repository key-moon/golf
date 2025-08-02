def p(g):
	B=next(filter(None,g[-1]));C=g[-1].index(B)
	for A in range(C,10,2):
		for D in range(10):g[D][A]=B
	for(E,A)in enumerate(range(C+1,10,2)):g[(E&1)*9][A]=5
	return g