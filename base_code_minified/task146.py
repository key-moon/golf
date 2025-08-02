def p(g):
	for A in(0,3,6):
		if not g[A][0]==g[A+1][1]==g[A+2][2]:return g[A:A+3]