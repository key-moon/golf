def	p(g,v=range):
	C=[r[:]for	r	in	g]
	for	c	in	v(1,10):
		A=[(i,j)for	i	in	v(len(g))for	j	in	v(len(g[0]))if	g[i][j]==c]
		for	i	in	v(len(A)):
			for	j	in	v(i+1,len(A)):
				o,B=A[i];D,b=A[j]
				if	o==D:
					for	x	in	v(min(B,b),max(B,b)+1):C[o][x]=c
				elif	B==b:
					for	y	in	v(min(o,D),max(o,D)+1):C[y][B]=c
	return	C