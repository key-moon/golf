def	p(m):
	r=len(m);c=len(m[0]);A=[i[:]for	i	in	m]
	for	j	in	range(c):
		B=[i	for	i	in	range(r)if	m[i][j]];l=len(B)//2
		for	i	in	range(l):A[B[-1-i]][j]=8
	return	A