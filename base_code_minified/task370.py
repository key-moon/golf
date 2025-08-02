def p(g):
	F=g[0][0];G,H=len(g),len(g[0])
	for A in range(G):
		for B in range(H):
			C=g[A][B]
			if C-F and C:I,J,K=A,B,C;break
		else:continue
		break
	for(D,E)in((1,1),(1,-1),(-1,1),(-1,-1)):
		A,B=I,J
		while 0<=A+D<G and 0<=B+E<H and g[A+D][B+E]==F:A+=D;B+=E;g[A][B]=K
	return g