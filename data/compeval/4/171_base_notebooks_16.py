def	p(j,A=range):
	c=len(j);C=len(j[0]);k=[[0for	A	in	A(C)]for	B	in	A(c)]
	for	B	in	A(c):
		for	l	in	A(C):
			if	B==0	or	B==c-1or	l==0	or	l==C-1:k[B][l]=8
			else:k[B][l]=0
	return	k