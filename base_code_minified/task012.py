def p(g):
	for A in range(2,len(g)-2):
		for B in range(2,len(g)-2):
			D=g[A][B]
			if D and g[A-1][B]==g[A+1][B]==g[A][B-1]==g[A][B+1]!=D:
				E=g[A-1][B]
				for C in(1,2,-1,-2):g[A+C][B]=E;g[A][B+C]=E;g[A+C][B+C]=D;g[A+C][B-C]=D
	return g