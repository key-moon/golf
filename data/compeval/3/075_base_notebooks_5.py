def	p(j):
	A=range;c=[A[:]for	A	in	j];D=[[j[k][A]for	A	in	A(3)]for	k	in	A(3)]
	for	k	in	A(9):
		for	B	in	A(4,13):
			if	j[k][B]==1:
				for	l	in	A(-1,2):
					for	C	in	A(-1,2):
						if	0<=k+l<9and	4<=B+C<13:c[k+l][B+C]=D[l+1][C+1]
	return	c