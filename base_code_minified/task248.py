def p(g):
	A=len(g[0]);C=2*A-2;E=-9%C
	for D in range(10):B=(D+E)%C;g[D]=[(B<A and B or 2*A-2-B)==C for C in range(A)]
	return g