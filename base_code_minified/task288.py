def p(A):
	B=len(A)-1;C=next(C for C in A[B]if C and C not in A[B-1]);E=[A for(A,B)in enumerate(A[B])if B==C];I,J=E[0],E[-1];K=len(A[0])
	for D in range(1,B):
		F=B-D-1;G=I-D
		if G>=0:A[F][G]=C
		H=J+D
		if H<K:A[F][H]=C
	return A