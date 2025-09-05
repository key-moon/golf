def	p(g):
	m={}
	for(i,r)in	enumerate(g):
		for(j,v)in	enumerate(r):
			if	v:a=m.setdefault(v,[i,i,j,j]);a[0]=min(a[0],i);a[1]=max(a[1],i);a[2]=min(a[2],j);a[3]=max(a[3],j)
	for(v,a)in	m.items():
		for	i	in	range(a[0],a[1]+1):
			for	j	in	range(a[2],a[3]+1):g[i][j]=v
	return	g