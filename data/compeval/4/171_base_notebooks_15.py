def	p(g,K=range):
	C=len(g);D=len(g[0]);E=[[0for	A	in	K(D)]for	A	in	K(C)]
	for	A	in	K(C):
		for	B	in	K(D):
			if	A==0	or	A==C-1or	B==0	or	B==D-1:E[A][B]=8
			else:E[A][B]=0
	return	E