def	p(g,K=range):
	h,w=len(g),len(g[0]);m=[[0]*w	for	_	in	K(h)]
	for	j	in	K(w):
		b=[g[i][j]for	i	in	K(h)if	g[i][j]!=0]
		for(k,v)in	enumerate(b):m[k][j]=v
	return	m