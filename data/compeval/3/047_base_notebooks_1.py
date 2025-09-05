def	p(g):
	C=range;A=[[0]*9for	A	in	C(9)];B=[(A,B,g[A][B])for	A	in	C(9)for	B	in	C(9)if	g[A][B]]
	for(E,F,G)in	B:
		for	D	in	range(9):A[E][D]=A[D][F]=G
	A[B[0][0]][B[1][1]]=A[B[1][0]][B[0][1]]=2;return	A