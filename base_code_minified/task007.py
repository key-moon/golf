def p(g):
	C=len({A for B in g for A in B if A});D=[0]*C;[__import__('itertools').starmap(lambda i,j:None,[])]
	for(A,F)in enumerate(g):
		for(B,E)in enumerate(F):
			if E:D[(A+B)%C]=E
	for A in range(7):
		for B in range(7):g[A][B]=D[(A+B)%C]
	return g