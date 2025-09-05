def	p(g):
	m=len({v	for	A	in	g	for	v	in	A	if	v});s=[0]*m
	for(i,A)in	enumerate(g):
		for(j,v)in	enumerate(A):
			if	v:s[(i+j)%m]=v
	return[[s[(i+j)%m]for	j	in	range(len(g[0]))]for	i	in	range(len(g))]