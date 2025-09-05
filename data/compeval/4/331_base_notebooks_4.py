def	p(g):
	B=[];C=enumerate
	for(r,D)in	C(g):
		for(c,F)in	C(D):
			if	g[r][c]==1:B.append([r,c])
	for	E	in	B:
		u,A=E
		if	u>0:g[u-1][A]=2
		if	u<9:g[u+1][A]=8
		if	A>0:g[u][A-1]=7
		if	A<9:g[u][A+1]=6
	return	g