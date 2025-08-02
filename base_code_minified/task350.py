def p(A):
	for(D,E)in enumerate(A):
		B=[A for(A,B)in enumerate(E)if B==1]
		if B:
			for C in range(B[0]+1,B[-1]):E[C]=8
	for C in range(len(A[0])):
		B=[B for B in range(len(A))if A[B][C]==1]
		if B:
			for D in range(B[0]+1,B[-1]):A[D][C]=8
	return A