def	p(j):
	B=range;c=[[0]*9for	c	in	B(9)];A=[(c,A,j[c][A])for	c	in	B(9)for	A	in	B(9)if	j[c][A]]
	for(k,D,l)in	A:
		for	C	in	range(9):c[k][C]=c[C][D]=l
	c[A[0][0]][A[1][1]]=c[A[1][0]][A[0][1]]=2;return	c