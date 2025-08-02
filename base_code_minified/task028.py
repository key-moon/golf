def p(A):
	D=len(A);E=sorted((B,D,A)for(B,C)in enumerate(A)for(D,A)in enumerate(C)if A);F,J,G=E[0];H,J,I=E[-1]
	for C in range(1,D-1):A[C][0]=A[C][-1]=G if C*2<=F+H else I
	for B in range(D):A[0][B]=A[F][B]=G;A[H][B]=A[-1][B]=I
	return A