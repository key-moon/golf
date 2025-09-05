def	p(j):
	D=[A[:]for	A	in	j];c,E=len(j),len(j[0])
	for	k	in	range(c):
		for	B	in	range(E):
			if	j[k][B]:
				l=j[k][B]
				for	A	in[(-1,-1),(-1,1),(1,1),(1,-1)]:
					a,C=k+A[0],B+A[1]
					while	0<=a<c	and	0<=C<E:D[a][C]=l;a+=A[0];C+=A[1]
	return	D