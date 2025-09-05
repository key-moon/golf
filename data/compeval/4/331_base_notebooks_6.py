def	p(g):
	C=[];D=enumerate
	for(r,E)in	D(g):
		for(c,F)in	D(E):
			if	g[r][c]==1:C.append([r,c])
	for	v	in	C:
		A,B=v
		if	A>0:g[A-1][B]=2
		if	A<9:g[A+1][B]=8
		if	B>0:g[A][B-1]=7
		if	B<9:g[A][B+1]=6
	return	g