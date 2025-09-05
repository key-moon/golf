def	p(g):
	A=range;F=[A[:]for	A	in	g];I=g[5][0];G=[[g[B+1][A+1]for	A	in	A(3)]for	B	in	A(3)]
	for	H	in[(0,6),(0,12),(6,0),(6,6),(6,12),(12,0),(12,6),(12,12)]:
		for	B	in	A(3):
			for	C	in	A(3):D,E=H[0]+B+1,H[1]+C+1;F[D][E]=g[D][E]if	G[B][C]==g[D][E]else	I	if	G[B][C]else	0
	return	F