def p(g):
	F,G={},{}
	for(A,H)in enumerate(g):
		for(B,C)in enumerate(H):
			if C:F.setdefault(A,[]).append(B);G.setdefault(B,[]).append(A)
	for(A,D)in F.items():
		if len(D)==2:
			C,E=sorted(D)
			for B in range(C,E+1):g[A][B]=8
	for(B,D)in G.items():
		if len(D)==2:
			C,E=sorted(D)
			for A in range(C,E+1):g[A][B]=8
	return g