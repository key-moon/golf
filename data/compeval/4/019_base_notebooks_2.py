j=len
A=range
def	p(c):
	c=[A[:]+A[:]for	A	in	c]+[A[:]+A[:]for	A	in	c];D,k=j(c),j(c[0])
	for	B	in	A(D):
		for	l	in	A(k):
			E=c[B][l]
			if	E>0and	E!=8:
				for(a,C)in[[1,1],[-1,-1],[-1,1],[1,-1]]:
					if	a+B>=0and	C+l>=0and	a+B<D	and	C+l<k:
						if	c[a+B][C+l]==0:c[a+B][C+l]=8
	return	c