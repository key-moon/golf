def p(g):
	D={}
	for(A,I)in enumerate(g):
		for(B,C)in enumerate(I):
			if C:E,F,G,H=D.get(C,(A,A,B,B));D[C]=min(E,A),max(F,A),min(G,B),max(H,B)
	for(C,(E,F,G,H))in D.items():
		for A in range(E+1,F):
			for B in range(G+1,H):
				if g[A][B]==C:g[A][B]=0
	return g