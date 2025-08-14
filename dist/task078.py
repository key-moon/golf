def	p(g,K=range):
	B,C=len(g),len(g[0]);D=[[0]*C	for	A	in	K(B)]
	for	A	in	K(C):
		E=[g[B][A]for	B	in	K(B)if	g[B][A]!=0]
		for(F,G)in	enumerate(E):D[F][A]=G
	return	D