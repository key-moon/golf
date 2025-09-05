def	p(g,u=range):
	A=enumerate;C,D=len(g),len(g[0]);z=[[0]*D	for	_	in	u(C)];t={v	for	A	in	g	for	v	in	A	if	v}
	for	c	in	t:
		B=[i	for(i,A)in	A(g)for	v	in	A	if	v==c];b=[j	for(i,B)in	A(g)for(j,v)in	A(B)if	v==c];k,o=min(B),max(B)+1;E,y=min(b),max(b)+1
		for	i	in	u(k,o):
			for	j	in	u(E,y):z[i][j]=c
	return	z