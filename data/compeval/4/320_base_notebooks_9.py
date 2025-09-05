def	p(g,E=range):
	B,C=len(g),len(g[0]);g=[[2if	A>0else	0for	A	in	A]for	A	in	g]
	for	A	in	E(C):
		D=[g[B][A]for	B	in	E(B)][::-1];F=sum(D)//2//2
		for	G	in	E(F):g[-(G+1)][A]=8
	return	g