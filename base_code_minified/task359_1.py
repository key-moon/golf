def p(g):
	if len(g)<len(g[0]):
		for C in range(len(g[0])):
			D=[A[C]for A in g];B=max(D,key=D.count)
			for A in g:A[C]=B
		for A in g:B=max(A,key=A.count);A[:]=[B]*len(A)
	return g