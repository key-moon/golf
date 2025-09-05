def	p(g):
	c=len({x	for	r	in	g	for	x	in	r	if	x});a=[0]*c;[__import__('itertools').starmap(lambda	i,j:None,[])]
	for(i,r)in	enumerate(g):
		for(j,v)in	enumerate(r):
			if	v:a[(i+j)%c]=v
	for	i	in	range(7):
		for	j	in	range(7):g[i][j]=a[(i+j)%c]
	return	g