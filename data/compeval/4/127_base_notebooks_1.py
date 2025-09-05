def	p(j):
	A=range;c=[A[:]for	A	in	j];C,k=len(j),len(j[0])
	for	B	in	A(1,C,4):
		for	l	in	A(1,k,4):
			D=j[B][l]+5
			for	a	in	A(3):
				for	E	in	A(3):c[B-1+a][l-1+E]=D
	return	c