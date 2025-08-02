def p(A):
	C=[(A,C)for(A,B)in enumerate(A)for(C,D)in enumerate(B)if D==8]
	for D in{A for(A,B)in C}:
		B=[B for(A,B)in C if A==D];F,G=min(B),max(B)
		for E in range(F,G+1):A[D][E]=8
	for E in{A for(B,A)in C}:
		B=[A for(A,B)in C if B==E];F,G=min(B),max(B)
		for D in range(F,G+1):A[D][E]=8
	return A