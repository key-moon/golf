def	p(g):
	h=len(g);A=[r[:]for	r	in	g]
	for	i	in	range(h//2):A[h-1-i]=A[i][:]
	return	A