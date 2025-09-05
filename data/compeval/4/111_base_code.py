def	p(g):
	for(i,r)in	enumerate(g):
		if	5in	r:c=r.index(5);break
	return[x[c-1:c+2]for	x	in	g[i+1:i+4]]