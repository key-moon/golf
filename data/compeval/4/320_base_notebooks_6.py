def	p(j,A=range):
	c=len(j);C=len(j[0]);p=[A[:]for	A	in	j]
	for	k	in	A(C):
		B=[A	for	A	in	A(c)if	j[A][k]];l=len(B)//2
		for	D	in	A(l):p[B[-1-D]][k]=8
	return	p