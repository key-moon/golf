def	p(j):
	B,c,C=j;k=6,4,0,0,0,1,3,1,0,0,0,4
	for	A	in	range(len(B)):
		l=k[A%12]
		if	l&1:B[A]=4
		if	l&2:c[A]=4
		if	l&4:C[A]=4
	return	j