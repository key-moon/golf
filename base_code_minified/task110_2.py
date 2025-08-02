def p(A):
	B,C=len(A),len(A[0]);D=A[0];H=next(A for A in range(1,C)if all(D[B]and D[B]==D[B+A]for B in range(C-A)));E=[A[B][0]for B in range(B)];I=next(A for A in range(1,B)if all(E[B]and E[B]==E[B+A]for B in range(B-A)))
	for F in range(B):
		for G in range(C):
			if A[F][G]==0:A[F][G]=A[F%I][G%H]
	return A