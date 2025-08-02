def p(A):
	J,K=len(A),len(A[0]);F=[(C,B)for C in range(J)for B in range(K-4)if A[C][B:B+5]==[4]*5];B,C=F[0];D,E=F[1]
	if not any(A[B+D][C+E]for D in(1,-1)for E in range(5)):B,C,D,E=D,E,B,C
	for G in(1,-1):
		for H in range(5):
			I=A[B+G][C+H]
			if I:A[D-G][E+H]=I
	return A