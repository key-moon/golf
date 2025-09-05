j=len
A=range
def	p(c):
	D,k=j(c),j(c[0])
	for	B	in	A(D):
		for	l	in	A(k):
			if	c[B][l]==2:
				for(C,a)in[[1,1],[-1,-1],[-1,1],[1,-1]]:c[C+B][a+l]=4
			if	c[B][l]==1:
				for(C,a)in[[0,1],[0,-1],[-1,0],[1,0]]:c[C+B][a+l]=7
	return	c