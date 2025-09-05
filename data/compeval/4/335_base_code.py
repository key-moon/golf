def	p(g):
	for(y,r)in	enumerate(g):
		for(x,v)in	enumerate(r):
			if	v==8:A,C=x,y
			if	v==2:D,B=x,y
	E=(B>C)-(B<C)
	for	y	in	range(C+E,B+E,E):g[y][A]=4
	F=(D>A)-(D<A)
	for	x	in	range(A+F,D,F):g[B][x]=4
	return	g