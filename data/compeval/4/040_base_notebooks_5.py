def	p(g):
	q=range;r=[o[:]for	o	in	g];h=g[0][0]==g[0][9];a,b=(g[0][0],g[9][0])if	h	else(g[0][0],g[0][9]);x=next(v	for	A	in	g	for	v	in	A	if	v	and	v	not	in[a,b])
	for	i	in	q(10):
		for	j	in	q(10):
			if	g[i][j]==x:d=(i,9-i)if	h	else(j,9-j);r[i][j]=a	if	d[0]<d[1]else	b
	return	r