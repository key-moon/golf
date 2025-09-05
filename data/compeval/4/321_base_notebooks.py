def	p(j):
	for	A	in	range(4):
		for	c	in	range(4):
			if	j[A][c+5]>0:j[A][c+10]=j[A][c+5]
			if	j[A][c]>0:j[A][c+10]=j[A][c]
	return[A[10:]for	A	in	j]