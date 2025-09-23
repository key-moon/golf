def p(g,R=range):
	g=[[A for A in A if A>0]for A in g if A.count(0)<2];g=[[A[0]]*10 for A in g+g+g]
	for A in R(10):
		for B in R(10):g[A][B]=g[B][A]
	return g[:10]