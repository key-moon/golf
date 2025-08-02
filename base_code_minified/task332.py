def p(g):
	D=len(g[0])&1^1
	for A in g:
		for(B,C)in enumerate(A):A[B]=C-2*(C==5 and B&1==D)
	return g