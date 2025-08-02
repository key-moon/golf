def p(g):
	for A in g:
		for(C,B)in enumerate(A):
			if B:
				for D in range(C+1,len(A)):A[D]=B+(5-B)*(D-C&1)
	return g