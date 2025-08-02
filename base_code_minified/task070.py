def p(g):
	A,B=zip(*[(A,C)for(A,B)in enumerate(g)for(C,D)in enumerate(B)if D==8]);E,F=min(A),max(A);G,H=min(B),max(B)
	for C in range(E,F+1):
		for D in range(G,H+1):
			if g[C][D]^8:g[C][D]=3
	return g