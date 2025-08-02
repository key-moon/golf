def p(A):
	B=len(A)//2
	for C in range(B):
		E,F=A[C],A[C+B+1]
		for(G,D)in enumerate(F):
			if D:E[G]=D
	A[:]=A[:B];return A