def	p(g,R=range,E=enumerate):
	C=len(g);D=len(g[0]);a=[[0]*D	for	_	in	R(C)];r={v	for	A	in	g	for	v	in	A	if	v}
	for	c	in	r:
		A=[i	for(i,A)in	E(g)for	v	in	A	if	v==c];B=[j	for(i,A)in	E(g)for(j,v)in	E(A)if	v==c];F,G=min(A),max(A)+1;b,H=min(B),max(B)+1
		for	i	in	R(F,G):
			for	j	in	R(b,H):a[i][j]=c
	return	a