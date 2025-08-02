def p(g):
	for A in range(1,len(g)-1):
		for B in range(1,len(g)-1):
			C=g[A-1][B]
			if C==g[A+1][B]==g[A][B-1]==g[A][B+1]!=g[A][B]:g[A][B]=C;return[[g[A][B]for B in(B-1,B,B+1)]for A in(A-1,A,A+1)]