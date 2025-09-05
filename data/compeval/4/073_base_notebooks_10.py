def	p(j):
	A=[o[:]for	o	in	j]
	for	c	in	range(5):
		for	B	in	range(5):
			if	j[B][c]==1:A[B][c]=0;A[4][c]=1
	return	A