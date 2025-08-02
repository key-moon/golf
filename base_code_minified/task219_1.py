def p(A):
	for(B,E)in((5,1),(10,2)):
		D=[B for B in range(B,B+5)if any(A[B][C]==8 for C in range(10))]
		if not D:continue
		F=D[-1]+E
		for C in range(10):
			if any(A[B][C]==8 for B in range(5))and all(A[B][C]!=8 for B in range(B,B+5)):A[F][C]=1
	return A