def p(g):
	for A in range(len(g)-1):g[A][-1-A]=2
	g[-1][1:]=[4]*(len(g)-1);return g