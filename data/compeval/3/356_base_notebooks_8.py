def	p(g,R=range,w=len):
	C=[r[:]for	r	in	g]
	for	c	in	R(1,10):
		A=[(i,j)for	i	in	R(w(g))for	j	in	R(w(g[0]))if	g[i][j]==c]
		for	i	in	R(w(A)):
			for	j	in	R(i+1,w(A)):
				v,B=A[i];D,a=A[j]
				if	v==D:
					for	x	in	R(min(B,a),max(B,a)+1):C[v][x]=c
				elif	B==a:
					for	y	in	R(min(v,D),max(v,D)+1):C[y][B]=c
	return	C