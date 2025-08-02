def p(val_g):
	B=val_g;C=[(A,C)for(A,B)in enumerate(B)for(C,D)in enumerate(B)if D==8]
	for D in{A for(A,B)in C}:
		A=[B for(A,B)in C if A==D];F,G=min(A),max(A)
		for E in range(F,G+1):B[D][E]=8
	for E in{A for(B,A)in C}:
		A=[A for(A,B)in C if B==E];F,G=min(A),max(A)
		for D in range(F,G+1):B[D][E]=8
	return B