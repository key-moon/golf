def p(A):
	for C in A:
		B=[A for(A,B)in enumerate(C)if B]
		for(D,E)in zip(B,B[1:]):
			for F in range(D+1,E):C[F]=2
	for(G,C)in enumerate(zip(*A)):
		B=[A for(A,B)in enumerate(C)if B]
		for(D,E)in zip(B,B[1:]):
			for F in range(D+1,E):A[F][G]=2
	return A