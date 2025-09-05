def	p(g):
	B=[A[:]for	A	in	g];E,D=len(g),len(g[0])
	for	A	in	range(D):
		if	g[0][A]:
			for	C	in	range(E):
				if	C%2==0:B[C][A]=g[0][A]
				else:
					if	A>0:B[C][A-1]=g[0][A]
					if	A<D-1:B[C][A+1]=g[0][A]
	return	B