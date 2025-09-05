def	p(g):
	D={}
	for(B,L)in	enumerate(g):
		for(C,E)in	enumerate(L):
			if	E:
				A=D.get(E)
				if	A:
					if	B<A[0]:A[0]=B
					if	B>A[1]:A[1]=B
					if	C<A[2]:A[2]=C
					if	C>A[3]:A[3]=C
				else:D[E]=[B,B,C,C]
	F=0,[]
	for(M,(G,H,I,J))in	D.items():
		K=[A[I:J+1]for	A	in	g[G:H+1]]
		if	all(A==A[::-1]for	A	in	K)and(H-G+1)*(J-I+1)>F[0]:F=(H-G+1)*(J-I+1),K
	return	F[1]