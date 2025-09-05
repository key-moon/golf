def	p(g):
	h,w=len(g),len(g[0]);g=[[2if	A>0else	0for	A	in	A]for	A	in	g]
	for	c	in	range(w):
		A=[g[r][c]for	r	in	range(h)][::-1];r=sum(A)//2//2
		for	i	in	range(r):g[-(i+1)][c]=8
	return	g