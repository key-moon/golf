def p(g):
	F={}
	for(A,H)in enumerate(g):
		for(B,C)in enumerate(H):
			if C:F.setdefault(C,[]).append((A,B))
	for(C,G)in F.items():
		A,B=G[0];D,E=G[1];I=(D>A)-(D<A);J=(E>B)-(E<B)
		while 1:
			g[A][B]=C
			if A==D and B==E:break
			A+=I;B+=J
	return g