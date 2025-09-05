def	p(g,F=range):
	C=[r[:]for	r	in	g]
	for	c	in	F(1,10):
		s=[(i,j)for	i	in	F(len(g))for	j	in	F(len(g[0]))if	g[i][j]==c]
		for	i	in	F(len(s)):
			for	j	in	F(i+1,len(s)):
				A,B=s[i];m,a=s[j]
				if	A==m:
					for	x	in	F(min(B,a),max(B,a)+1):C[A][x]=c
				elif	B==a:
					for	y	in	F(min(A,m),max(A,m)+1):C[y][B]=c
	return	C