def p(g):
	D,E,F,G=g[0][1],g[-1][1],g[1][0],g[1][-1]
	for A in range(1,len(g)-1):
		for B in range(1,len(g[0])-1):
			C=g[A][B]
			if C==D:g[1][B]=D
			elif C==E:g[-2][B]=E
			elif C==F:g[A][1]=F
			elif C==G:g[A][-2]=G
			g[A][B]=0
	return g