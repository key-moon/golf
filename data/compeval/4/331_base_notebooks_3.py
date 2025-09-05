def	p(g):
	B=[];C=enumerate
	for(r,D)in	C(g):
		for(c,E)in	C(D):
			if	g[r][c]==1:B.append([r,c])
	for	n	in	B:
		A,k=n
		if	A>0:g[A-1][k]=2
		if	A<9:g[A+1][k]=8
		if	k>0:g[A][k-1]=7
		if	k<9:g[A][k+1]=6
	return	g