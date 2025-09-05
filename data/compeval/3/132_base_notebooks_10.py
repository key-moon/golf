def	p(g,k=range):
	A=enumerate;D,E=len(g),len(g[0]);b=[[0]*E	for	_	in	k(D)];s={v	for	m	in	g	for	v	in	m	if	v}
	for	c	in	s:
		B=[i	for(i,m)in	A(g)for	v	in	m	if	v==c];C=[j	for(i,m)in	A(g)for(j,v)in	A(m)if	v==c];F,n=min(B),max(B)+1;G,H=min(C),max(C)+1
		for	i	in	k(F,n):
			for	j	in	k(G,H):b[i][j]=c
	return	b