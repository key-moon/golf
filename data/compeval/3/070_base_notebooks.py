def	p(j):
	B=range;c=[A[:]for	A	in	j];A=[(A,c)for	A	in	B(len(j))for	c	in	B(len(j[0]))if	j[A][c]==8]
	if	A:
		k,D=min(A	for(A,B)in	A),max(A	for(A,B)in	A);l,E=min(A	for(B,A)in	A),max(A	for(B,A)in	A)
		for	a	in	B(k,D+1):
			for	C	in	B(l,E+1):
				if	j[a][C]==1:c[a][C]=3
	return	c