def	p(g):
	A=[];B=enumerate
	for(r,C)in	B(g):
		for(c,D)in	B(C):
			if	D==5:
				if	c	not	in	A:A.append(c)
				g[r][c]=A.index(c)+1
	return	g