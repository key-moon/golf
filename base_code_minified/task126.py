def p(g):
	for(A,B)in enumerate(zip(*g[:-1])):
		if len(g)-1-B.count(0)&1:g[-1][A]=4
	return g