def p(A):
	import math as I;J,G=len(A),len(A[0]);H=[(B,D,A)for(B,C)in enumerate(A)for(D,A)in enumerate(C)if A];B=sorted({A for(A,B,B)in H});C=sorted({B for(A,B,A)in H})
	if len(B)>1:
		E=B[1]-B[0]
		for D in range(2,len(B)):E=I.gcd(E,B[D]-B[D-1])
	else:E=J-1-B[0]
	if len(C)>1:
		F=C[1]-C[0]
		for D in range(2,len(C)):F=I.gcd(F,C[D]-C[D-1])
	else:F=G-1-C[0]
	K=[[0]*G for A in A]
	for(L,M,N)in H:
		for D in range(L,J,E):
			for O in range(M,G,F):K[D][O]=N
	return K