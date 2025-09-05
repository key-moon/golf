def	p(g):
	for	r	in	g:
		for	c	in	r:
			if	c:
				for	i	in	range(r.index(c),len(r)-1-r[::-1].index(c)+1):r[i]=c
	return	g