def	p(g):
	B=[];C=enumerate
	for(r,D)in	C(g):
		for(c,F)in	C(D):
			if	g[r][c]==1:B.append([r,c])
	for	E	in	B:
		m,A=E
		if	m>0:g[m-1][A]=2
		if	m<9:g[m+1][A]=8
		if	A>0:g[m][A-1]=7
		if	A<9:g[m][A+1]=6
	return	g