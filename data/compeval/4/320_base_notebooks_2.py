def	p(g,j=range):
	h,w=len(g),len(g[0]);g=[[2if	A>0else	0for	A	in	A]for	A	in	g]
	for	c	in	j(w):
		A=[g[r][c]for	r	in	j(h)][::-1];r=sum(A)//2//2
		for	i	in	j(r):g[-(i+1)][c]=8
	return	g