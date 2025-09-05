def	p(j):
	B=[o[:]for	o	in	j];c,C=len(j),len(j[0])
	for	k	in	range(1,c):
		for	A	in	range(1,C-1):
			if	j[k][A]==0and	j[k][A-1]and	j[k][A+1]and	j[k][A-1]==j[k][A+1]and	j[k-1][A]==j[k][A-1]:B[c-1][A]=4
	return	B