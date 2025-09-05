def	p(g):
	C=len(g);E=sorted({g[i][j]for	i	in	range(C)for	j	in	range(C)if	g[i][j]})
	for	D	in	E:
		H=[(i,j)for	i	in	range(C)for	j	in	range(C)if	g[i][j]==D];F,G=zip(*H);I,J=min(F),max(F);K,L=min(G),max(G)
		if	D==E[0]:
			A,B=I,K
			while	A	and	B:A-=1;B-=1;g[A][B]=D
		else:
			A,B=J,L
			while	A<C-1and	B<C-1:A+=1;B+=1;g[A][B]=D
	return	g