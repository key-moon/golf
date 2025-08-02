def p(A):
	from math import gcd;L,M=len(A),len(A[0]);B=[(B,D,A)for(B,C)in enumerate(A)for(D,A)in enumerate(C)if A];N=B[0][2];C=sorted({A for(A,B,B)in B});D=sorted({B for(A,B,A)in B});E=0
	for(F,G)in zip(C,C[1:]):E=gcd(E,G-F)
	H=0
	for(F,G)in zip(D,D[1:]):H=gcd(H,G-F)
	I=max(E,H);O,P=C[0],D[0]
	for J in range(L):
		for K in range(M):A[J][K]=N if(J-O)%I==0 or(K-P)%I==0 else 0
	return A