def	p(g):
	C=len(g);D=len(g[0]);H=0
	for	A	in	range(C):
		for	B	in	range(D):
			E=g[A][B]
			if	E:
				for	F	in	range(A,C):
					for	G	in	range(B,D):
						I=(F-A+1)*(G-B+1)
						if	I>H	and	all(g[x][y]==E	for	x	in	range(A,F+1)for	y	in	range(B,G+1)):H=I;K,L,M,N,O=A,B,F,G,E
	J=[[0]*D	for	_	in	range(C)]
	for	x	in	range(K,M+1):
		for	y	in	range(L,N+1):J[x][y]=O
	return	J