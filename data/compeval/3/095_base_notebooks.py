def	p(g):
	r=[o[:]for	o	in	g];n=len(g)
	for	i	in	range(n):
		for	j	in	range(n):
			if	g[i][j]==5:
				for	A	in[-1,0,1]:
					for	B	in[-1,0,1]:
						if	A	or	B:
							C,D=i+A,j+B
							if	0<=C<n	and	0<=D<n:r[C][D]=1
	return	r