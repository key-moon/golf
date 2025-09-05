def	p(g):
	B={};[B.setdefault(v,[]).append((i,j))for(i,A)in	enumerate(g)for(j,v)in	enumerate(A)];A=[k	for(k,v)in	B.items()if	k	and	len(v)==1][0];D,C=B[A][0];J=[p	for(k,v)in	B.items()if	k	and	k!=A	for	p	in	v];E,F=zip(*J);G,K,H,I=min(E),max(E),min(F),max(F);L,M=len(g),len(g[0])
	if	C==H:
		for	j	in	range(I+1,M):g[D][j]=A
	elif	C==I:
		for	j	in	range(H):g[D][j]=A
	elif	D==G:
		for	i	in	range(K+1,L):g[i][C]=A
	else:
		for	i	in	range(G):g[i][C]=A
	return	g