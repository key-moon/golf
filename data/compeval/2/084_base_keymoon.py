def	p(g,i=1):
	for	r	in	g[:-1]:r[-i]=2;g[-1][i]=4;i+=1
	return	g