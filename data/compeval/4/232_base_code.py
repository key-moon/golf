def	p(g):
	for	A	in	g:
		try:B,D=next((i,v)for(i,v)in	enumerate(A)if	v)
		except:continue
		for	C	in	range(len(A)-B):A[B+C]=[D,5][C&1]
	return	g