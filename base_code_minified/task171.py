def p(g):
	g[0]=g[-1]=[8]*len(g[0])
	for A in g[1:-1]:A[0]=A[-1]=8
	return g