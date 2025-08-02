def p(A):
	E,F=A[0],A[-1];G=len(E)
	for C in range(1,len(A)-1):
		for D in range(1,G-1):
			B=A[C][D]
			if B==E[D]:A[1][D]=B
			if B==F[D]:A[-2][D]=B
			if B==A[C][0]:A[C][1]=B
			if B==A[C][-1]:A[C][-2]=B
	return A