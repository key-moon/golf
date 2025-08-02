def p(g):
	A=len(g[0])//2
	for B in g:B[A:]=B[:A][::-1]
	return g