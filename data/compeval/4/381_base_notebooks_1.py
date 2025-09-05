def	p(g,R=range):
	n=len(g)
	for	i	in	R(1,n-1):
		s=a=0
		for	j	in	R(n):
			x=g[i][j];s=[s,1][s<1and	x>1]
			if	s==1and	x<1:s=2;a=[a,j][~a]
			if	s>1and	x>1:
				for	u	in	R(a,j):g[i][u]=9;s=1;a=0
	return	g