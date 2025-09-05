def	p(g):
	h,w=len(g),len(g[0]);D=[i	for(i,A)in	enumerate(g)for	v	in	A	if	v];E=[j	for(i,A)in	enumerate(g)for(j,v)in	enumerate(A)if	v];A=[[0]*w	for	_	in	range(h)]
	for(i,j)in	zip(D,E):
		B,C=i+1,j+0
		if	0<=B<h	and	0<=C<w:A[B][C]=g[i][j]
	return	A