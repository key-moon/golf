def p(g):
	D,E=g[0],g[-1];F=len(D)
	for B in range(1,len(g)-1):
		for C in range(1,F-1):
			A=g[B][C]
			if A==D[C]:g[1][C]=A
			if A==E[C]:g[-2][C]=A
			if A==g[B][0]:g[B][1]=A
			if A==g[B][-1]:g[B][-2]=A
	return g