def	p(g):
	A=enumerate;m=len({v	for	k	in	g	for	v	in	k	if	v});s=[0]*m
	for(i,k)in	A(g):
		for(j,v)in	A(k):
			if	v:s[(i+j)%m]=v
	return[[s[(i+j)%m]for	j	in	range(len(g[0]))]for	i	in	range(len(g))]