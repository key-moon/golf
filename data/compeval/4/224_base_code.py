def	p(g):
	d,e=zip(*[(i,j)for(i,r)in	enumerate(g)for(j,v)in	enumerate(r)if	v==5]);a,b=min(d)+1,max(d)-1;c,f=min(e)+1,max(e)-1;k=next(v	for	r	in	g	for	v	in	r	if	v%5)
	for	j	in	range(c,f+1):g[a][j]=g[b][j]=k
	for	i	in	range(a,b+1):g[i][c]=g[i][f]=k
	return	g