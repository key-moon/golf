def	p(g):
	A,B=[],[]
	for	i	in	range(len(g)):
		for	j	in	range(len(g[0])):
			if	g[i][j]>0:A.append(i);B.append(j)
	if	not	A:return	g
	C,D=min(A),max(A)+1;E,F=min(B),max(B)+1;return[r[E:F]for	r	in	g[C:D]]