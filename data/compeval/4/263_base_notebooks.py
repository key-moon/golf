def	p(g):
	A=range;B=[[[g[D+B*3][A+C*3]for	A	in	A(3)]for	D	in	A(3)]for	B	in	A(len(g)//3)for	C	in	A(len(g[0])//3)]
	for	C	in	B:
		if[tuple(tuple(B[C][A]==0for	A	in	A(3))for	C	in	A(3))for	B	in	B].count(tuple(tuple(C[B][A]==0for	A	in	A(3))for	B	in	A(3)))==1:return	C