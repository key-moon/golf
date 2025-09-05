def	p(g,u=range):
	A=enumerate;D,E=len(g),len(g[0]);B=[[0]*E	for	_	in	u(D)];F={v	for	f	in	g	for	v	in	f	if	v}
	for	c	in	F:
		s=[i	for(i,f)in	A(g)for	v	in	f	if	v==c];C=[j	for(i,f)in	A(g)for(j,v)in	A(f)if	v==c];G,H=min(s),max(s)+1;e,I=min(C),max(C)+1
		for	i	in	u(G,H):
			for	j	in	u(e,I):B[i][j]=c
	return	B