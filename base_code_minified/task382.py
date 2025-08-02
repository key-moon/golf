def p(A):
	F,G=len(A),len(A[0])
	for H in range(F):
		if any(A==8 for A in A[H]):J=[A for(A,B)in enumerate(A[H])if B==8];K=H;break
	I=[C for B in range(F)for(C,D)in enumerate(A[B])if D==2];L=1 if I and sum(I)/len(I)<G/2 else-1;E=[[0]*G for A in range(F)]
	for B in range(F):
		for(C,M)in enumerate(A[B]):
			if M==2:E[B][C]=2
	D=J[:]
	for B in range(K,F):
		if any(A==2 for A in A[B]):D=[A+L for A in D]
		for C in D:
			if 0<=C<G and E[B][C]==0:E[B][C]=8
	D=J[:]
	for B in range(K-1,-1,-1):
		if any(A==2 for A in A[B]):D=[A+L for A in D]
		for C in D:
			if 0<=C<G and E[B][C]==0:E[B][C]=8
	return E