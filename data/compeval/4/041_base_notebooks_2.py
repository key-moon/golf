def	p(g,z=0):
	for	r	in	g:
		for(i,x)in	enumerate(r):
			if	x:z=(not	z)*x
			else:r[i]=z
	return	g