def p(g):
	A=len(g);D=[g[A][A]for A in range((A+1)//2)]
	for B in range(A):
		for C in range(A):g[B][C]=D[(min(B,C,A-1-B,A-1-C)-1)%len(D)]
	return g