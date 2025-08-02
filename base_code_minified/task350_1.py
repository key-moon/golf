def p(g):
	for D in g:
		A=-1
		for(B,F)in enumerate(D):
			if F:
				if A+1:
					for C in range(A+1,B):D[C]=D[C]or 8
				A=B
	G=len(g)
	for E in range(len(g[0])):
		A=-1
		for B in range(G):
			if g[B][E]:
				if A+1:
					for C in range(A+1,B):g[C][E]=g[C][E]or 8
				A=B
	return g