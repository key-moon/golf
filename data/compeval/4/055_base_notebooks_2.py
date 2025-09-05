def	p(m):
	F,G=len(m),len(m[0]);A=[r[:]for	r	in	m];B,C=[r	for	r	in	range(F)if	all(v==8for	v	in	m[r])];D,E=[c	for	c	in	range(G)if	all(m[r][c]==8for	r	in	range(F))]
	for	r	in	range(F):
		for	c	in	range(G):
			if	not	A[r][c]:
				if	r<B	and	D<c<E:A[r][c]=2
				elif	B<r<C	and	c<D:A[r][c]=4
				elif	B<r<C	and	D<c<E:A[r][c]=6
				elif	B<r<C	and	c>E:A[r][c]=3
				elif	r>C	and	D<c<E:A[r][c]=1
	return	A