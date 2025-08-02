def p(g):
	for A in{*sum(g,[])}-{0}:
		B,C=min(B for(B,C)in enumerate(g)for D in C if D==A),max(B for(B,C)in enumerate(g)for D in C if D==A);D,E=min(C for B in g for(C,D)in enumerate(B)if D==A),max(C for B in g for(C,D)in enumerate(B)if D==A)
		for F in range(B+1,C):
			for G in range(D+1,E):g[F][G]=8
	return g