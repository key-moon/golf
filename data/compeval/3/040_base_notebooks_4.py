def	p(g):
	C=range;D=[A[:]for	A	in	g];E=g[0][0]==g[0][9];F,G=(g[0][0],g[9][0])if	E	else(g[0][0],g[0][9]);I=next(A	for	B	in	g	for	A	in	B	if	A	and	A	not	in[F,G])
	for	A	in	C(10):
		for	B	in	C(10):
			if	g[A][B]==I:H=(A,9-A)if	E	else(B,9-B);D[A][B]=F	if	H[0]<H[1]else	G
	return	D