def	p(g):
	A=0;h,w=len(g),len(g[0])
	for	r	in	range(h-1):
		for	c	in	range(w-1):
			q=g[r][c:c+2]+g[r+1][c:c+2]
			if	q==[1,1,1,1]:A+=1
	return[[0if	i+1>A	else	1for	i	in	range(5)]]