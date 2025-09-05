def	p(j):
	B,c,C=len(j),len(j[0]),range;k=[(A,l)for	A	in(0,B-1)for	l	in	C(c)if	j[A][l]<1]+[(A,l)for	A	in	C(B)for	l	in(0,c-1)if	j[A][l]<1]
	while	k:
		A,l=k.pop()
		if	j[A][l]<1:j[A][l]=3;k+=[(x,y)for(x,y)in((A+1,l),(A-1,l),(A,l+1),(A,l-1))if	0<=x<B	and	0<=y<c	and	j[x][y]<1]
	for	A	in	C(B):
		for	l	in	C(c):
			if	j[A][l]<1:j[A][l]=2
	return	j