def p(A):
	B=A[0][0];K=next(A for C in A for A in C if A and A!=B);C=[(A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B];D=[(A,C)for(A,B)in enumerate(A)for(C,D)in enumerate(B)if D==K];E=[A for(A,B)in C];L=[A for(B,A)in C];M=[A for(A,B)in D];F=[A for(B,A)in D];N,G=min(E)+1,max(E);H,O=min(L)-1,max(F);P=max(M)
	for I in range(N,P):
		if 0==A[I][H]:A[I][H]=3
	for J in range(min(F)+1,O):
		if 0==A[G][J]:A[G][J]=3
	return A