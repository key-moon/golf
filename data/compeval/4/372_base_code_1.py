def	p(g):
	n=len(g)//2
	for	i	in	range(n):
		a,b=g[i],g[i+n+1]
		for(j,v)in	enumerate(b):
			if	v:a[j]=v
	g[:]=g[:n];return	g