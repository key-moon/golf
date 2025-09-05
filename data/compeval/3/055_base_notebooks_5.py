def	p(j,A=range):
	c,E=len(j),len(j[0]);k=[a[:]for	a	in	j];C,l=[a	for	a	in	A(c)if	all(v==8for	v	in	j[a])];p,D=[B	for	B	in	A(E)if	all(j[a][B]==8for	a	in	A(c))]
	for	a	in	A(c):
		for	B	in	A(E):
			if	not	k[a][B]:
				if	a<C	and	p<B<D:k[a][B]=2
				elif	C<a<l	and	B<p:k[a][B]=4
				elif	C<a<l	and	p<B<D:k[a][B]=6
				elif	C<a<l	and	B>D:k[a][B]=3
				elif	a>l	and	p<B<D:k[a][B]=1
	return	k