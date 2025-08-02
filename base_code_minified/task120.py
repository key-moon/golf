def p(g):
	for A in{A for B in g for A in B if A and A^8}:
		B=[B for(B,C)in enumerate(g)for D in C if D==A];C=[C for B in g for(C,D)in enumerate(B)if D==A];F,G=min(B),max(B);H,I=min(C),max(C)
		for D in range(F+1,G):
			for E in range(H+1,I):
				if g[D][E]==A:g[D][E]=8
	return g