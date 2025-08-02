def p(A):
	C=next(B for C in A for B in C if B and sum(C==B for A in A for C in A)==1);D,E=next((A,D)for(A,B)in enumerate(A)for(D,E)in enumerate(B)if E==C);I,F=len(A),len(A[0]);B=[[0]*F for A in A]
	for J in(-1,0,1):
		for K in(-1,0,1):
			G,H=D+J,E+K
			if 0<=G<I and 0<=H<F:B[G][H]=2
	B[D][E]=C;return B