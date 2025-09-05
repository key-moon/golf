def	p(g):
	A=[i	for(i,r)in	enumerate(g)for	v	in	r	if	v==8];B=[j	for	r	in	g	for(j,v)in	enumerate(r)if	v==8];C,D=min(A),max(A);E,F=min(B),max(B)
	for(y,G)in	enumerate(g):
		for(x,v)in	enumerate(G):
			if	v%8:
				if	x<E:g[y][E]=v
				elif	x>F:g[y][F]=v
				elif	y<C:g[C][x]=v
				elif	y>D:g[D][x]=v
	return	g