def p(g):
	B=list(zip(*[A[:3]for A in g][::-1]));C=list(zip(*B[::-1]))
	for A in(0,1,2):g[A][4:7]=B[A];g[A][8:]=C[A]
	return g