def	p(L,v=range):
	b=len(L);A=len(L[0]);B=[[0for	_	in	v(A)]for	_	in	v(b)]
	for	r	in	v(b):
		for	c	in	v(A):
			if	r==0	or	r==b-1or	c==0	or	c==A-1:B[r][c]=8
			else:B[r][c]=0
	return	B