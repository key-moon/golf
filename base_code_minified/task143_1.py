def p(A):
	C=[A for B in A for A in B if A];D=[A for A in set(C)if C.count(A)==7][0];B=[(B,C)for B in range(10)for C in range(10)if A[B][C]==D];H,I=min(A for(A,B)in B),min(A for(B,A)in B);B=[(A-H,B-I)for(A,B)in B]
	for J in set(C)-{D}:
		F=[(B,C)for B in range(10)for C in range(10)if A[B][C]==J];K,L=min(A for(A,B)in F),min(A for(B,A)in F)
		for(M,N)in B:
			G,E=K+M,L+N
			if 0<=G<10<E<10 or 0<=E<10:A[G][E]=D
	return A