def	p(g):
	A,B=len(g),len(g[0]);F=[i	for(i,A)in	enumerate(g)for	v	in	A	if	v];G=[j	for(i,A)in	enumerate(g)for(j,v)in	enumerate(A)if	v];C=[[0]*B	for	_	in	range(A)]
	for(i,j)in	zip(F,G):
		D,E=i+1,j+0
		if	0<=D<A	and	0<=E<B:C[D][E]=g[i][j]
	return	C