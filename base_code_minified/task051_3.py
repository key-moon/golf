def p(A):
	C={};[C.setdefault(E,[]).append((A,D))for(A,B)in enumerate(A)for(D,E)in enumerate(B)];B=[A for(A,B)in C.items()if A and len(B)==1][0];E,D=C[B][0];M=[D for(A,C)in C.items()if A and A!=B for D in C];H,I=zip(*M);J,N,K,L=min(H),max(H),min(I),max(I);O,P=len(A),len(A[0])
	if D==K:
		for F in range(L+1,P):A[E][F]=B
	elif D==L:
		for F in range(K):A[E][F]=B
	elif E==J:
		for G in range(N+1,O):A[G][D]=B
	else:
		for G in range(J):A[G][D]=B
	return A