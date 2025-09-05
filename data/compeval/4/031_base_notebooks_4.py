def	p(g):
	c=[(i,j)for(i,r)in	enumerate(g)for(j,x)in	enumerate(r)if	x]
	if	c:A=min(i	for(i,j)in	c);B=max(i	for(i,j)in	c);C=min(j	for(i,j)in	c);D=max(j	for(i,j)in	c);return[g[i][C:D+1]for	i	in	range(A,B+1)]
	return	g