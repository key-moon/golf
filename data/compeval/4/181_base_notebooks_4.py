def	p(g):
	A=range;B=[A[:]for	A	in	g];E=[[g[B][A+3]for	A	in	A(3)]for	B	in	A(3)];F=[A[::-1]for	A	in	E];G=0if	g[3][3]else	6
	for	C	in	A(3):
		for	D	in	A(3):B[C][G+D]=F[C][D]
	return	B