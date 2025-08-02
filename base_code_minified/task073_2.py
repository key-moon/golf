def p(g):
	for A in g[:-1]:
		for(B,C)in enumerate(A):
			if C==1:A[B]=0;g[-1][B]=1
	return g