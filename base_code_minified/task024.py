def p(g):
	B,C={},set()
	for(D,E)in enumerate(g):
		for(F,A)in enumerate(E):
			if A&1:B[D]=A
			elif A:C|={F}
	return[[B.get(A)or(D in C)*2 for(D,E)in enumerate(g[0])]for(A,D)in enumerate(g)]