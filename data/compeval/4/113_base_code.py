def	p(g):
	k=0
	while	any(g[k]):k+=1
	for	i	in	range(k):g[-i-1]=g[i]
	return	g