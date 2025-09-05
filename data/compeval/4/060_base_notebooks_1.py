def	p(g):
	A=[list(r)for	r	in	g];h,w=len(g),len(g[0])
	for	r	in	range(h):
		C=[(c,g[r][c])for	c	in	range(w)if	g[r][c]!=0]
		if	len(C)==2:
			(D,F),(E,G)=C;B=(D+E)//2
			for	i	in	range(D+1,B):A[r][i]=F
			A[r][B]=5
			for	i	in	range(B+1,E):A[r][i]=G
	return	A