def p(g):
	E,F=len(g),len(g[0]);D=()
	for A in range(1,E-1):
		for B in range(1,F-1):
			C=g[A][B]
			if C and g[A-1][B]==C==g[A+1][B]and g[A][B-1]==C==g[A][B+1]:D+=(A,B),
	for(A,B)in D:g[A][B]=0
	return g