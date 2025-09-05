def	p(g):
	n=len(g);A=sorted((i,j,v)for(i,r)in	enumerate(g)for(j,v)in	enumerate(r)if	v);a,_,u=A[0];b,_,w=A[-1]
	for	i	in	range(1,n-1):g[i][0]=g[i][-1]=u	if	i*2<=a+b	else	w
	for	j	in	range(n):g[0][j]=g[a][j]=u;g[b][j]=g[-1][j]=w
	return	g