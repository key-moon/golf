def p(A):
	B=len(A);C=len(A[0]);G=B//3;D=max(range(B),key=lambda F:sum(A[F][B]==8 for B in range(C)));H=[B for B in range(C)if A[D][B]==8]
	for I in(1,2):
		for E in H:
			F=D+I*G
			if A[F][E]==0:A[F][E]=1
	return A