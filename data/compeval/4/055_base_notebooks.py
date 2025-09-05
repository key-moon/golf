def	p(j,A=range):
	c,E=len(j),len(j[0]);k=[A[:]for	A	in	j];C,l=[A	for	A	in	A(c)if	all(A==8for	A	in	j[A])];D,a=[B	for	B	in	A(E)if	all(j[A][B]==8for	A	in	A(c))]
	for	B	in	A(c):
		for	e	in	A(E):
			if	not	k[B][e]:
				if	B<C	and	D<e<a:k[B][e]=2
				elif	C<B<l	and	e<D:k[B][e]=4
				elif	C<B<l	and	D<e<a:k[B][e]=6
				elif	C<B<l	and	e>a:k[B][e]=3
				elif	B>l	and	D<e<a:k[B][e]=1
	return	k