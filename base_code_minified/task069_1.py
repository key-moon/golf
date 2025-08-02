def p(A):
	B=[(B,D,A)for(B,C)in enumerate(A)for(D,A)in enumerate(C)if A and A!=8]
	if not B:return A
	C=min(A for(A,B,C)in B);D=min(A for(B,A,C)in B);E=[(A-C,B-D,E)for(A,B,E)in B];F=[(C,B)for(C,D)in enumerate(A)for(B,E)in enumerate(D)if E==8 and(C==0 or A[C-1][B]!=8)and(B==0 or D[B-1]!=8)]
	for(G,H)in enumerate(A):A[G]=[0]*len(H)
	for(I,J)in F:
		for(K,L,M)in E:A[I+K][J+L]=M
	return A