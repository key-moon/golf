def p(g):
	C={}
	for(A,K)in enumerate(g):
		for(B,H)in enumerate(K):
			if H:I=C.setdefault(H,(set(),set()));I[0].add(A);I[1].add(B)
	G=D=0
	for(J,(E,F))in C.items():
		if len(E)<len(F):G=J
		else:D=J
	E,F=C[G][0],C[D][1];A,B=next(iter(E)),next(iter(F));L=G if g[A][B]==D else D
	for A in E:
		for B in F:g[A][B]=L
	return g