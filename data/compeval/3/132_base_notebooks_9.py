def	p(g):
	D,E=len(g),len(g[0]);A=[[0]*E	for	_	in	range(D)];F={v	for	A	in	g	for	v	in	A	if	v}
	for	c	in	F:
		B=[i	for(i,A)in	enumerate(g)for	v	in	A	if	v==c];C=[j	for(i,A)in	enumerate(g)for(j,v)in	enumerate(A)if	v==c];G,H=min(B),max(B)+1;I,J=min(C),max(C)+1
		for	i	in	range(G,H):
			for	j	in	range(I,J):A[i][j]=c
	return	A