def	p(g):
	r=[-1]+[i	for	i	in	range(len(g))if	g[i]==[5]*len(g[0])]+[len(g)];c=[-1]+[j	for	j	in	range(len(g[0]))if	all(g[i][j]==5for	i	in	range(len(g)))]+[len(g[0])]
	for(a,b)in	zip(r,r[1:]):
		for(x,y)in	zip(c,c[1:]):
			v=sum(g[i][j]for	i	in	range(a+1,b)for	j	in	range(x+1,y))+5
			for	i	in	range(a+1,b):g[i][x+1:y]=[v]*(y-x-1)
	return	g