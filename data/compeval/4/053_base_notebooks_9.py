def	p(g):
	h,w=len(g),len(g[0]);A=[[0]*w	for	_	in	range(h)]
	for	i	in	range(h):
		for	j	in	range(w):
			if	g[i][j]!=0:
				B,C=i+1,j+0
				if	0<=B<h	and	0<=C<w:A[B][C]=g[i][j]
	return	A