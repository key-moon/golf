def	p(g):
	B=range;C=[A[:]for	A	in	g];A=[(A,C)for	A	in	B(len(g))for	C	in	B(len(g[0]))if	g[A][C]==8]
	if	A:
		F,G=min(A	for(A,B)in	A),max(A	for(A,B)in	A);H,I=min(A	for(B,A)in	A),max(A	for(B,A)in	A)
		for	D	in	B(F,G+1):
			for	E	in	B(H,I+1):
				if	g[D][E]==1:C[D][E]=3
	return	C