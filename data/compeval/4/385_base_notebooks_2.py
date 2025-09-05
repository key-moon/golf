def	p(g,E=enumerate):
	for(r,A)in	E(g):
		for(c,B)in	E(A):
			if	r<len(g)//2:g[r][c]=g[-(r+1)][c]
	return	g