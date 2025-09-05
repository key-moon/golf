def	p(g):
	A=enumerate;m=len({v	for	u	in	g	for	v	in	u	if	v});s=[0]*m
	for(i,u)in	A(g):
		for(j,v)in	A(u):
			if	v:s[(i+j)%m]=v
	return[[s[(i+j)%m]for	j	in	range(len(g[0]))]for	i	in	range(len(g))]