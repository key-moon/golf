def p(A):
	E,B=len(A),len(A[0])
	for C in range(E):
		for F in range(B):
			if(G:=A[C][F]):
				for D in range(F,B):A[C][D]=G
				for D in range(C,E):A[D][B-1]=G
	return A