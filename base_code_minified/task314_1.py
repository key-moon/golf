def p(A):
	E=len(A)
	for B in range(E):
		for C in range(E):
			D=A[B][C]
			if D>1:
				for F in range(B+1,E):
					if A[F][C]==D:A[B+F>>1][C]=D
				for G in range(C+1,E):
					if A[B][G]==D:A[B][C+G>>1]=D
	return A