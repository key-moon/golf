def	p(g,D=range):
	A=enumerate;E,F=len(g),len(g[0]);B=[[0]*F	for	_	in	D(E)];G={v	for	A	in	g	for	v	in	A	if	v}
	for	c	in	G:
		b=[i	for(i,A)in	A(g)for	v	in	A	if	v==c];C=[j	for(i,B)in	A(g)for(j,v)in	A(B)if	v==c];e,z=min(b),max(b)+1;H,o=min(C),max(C)+1
		for	i	in	D(e,z):
			for	j	in	D(H,o):B[i][j]=c
	return	B