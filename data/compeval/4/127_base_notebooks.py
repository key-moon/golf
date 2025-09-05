def	p(g):
	A=range;B=[A[:]for	A	in	g];E,F=len(g),len(g[0])
	for	C	in	A(1,E,4):
		for	D	in	A(1,F,4):
			G=g[C][D]+5
			for	H	in	A(3):
				for	I	in	A(3):B[C-1+H][D-1+I]=G
	return	B