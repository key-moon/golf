def p(A):
	K,L=len(A),len(A[0]);M=0
	for R in{B for A in A for B in A}-{0}:
		B=[(B,C)for B in range(K)for C in range(L)if A[B][C]==R]
		if B:
			C=min(A for(A,B)in B);D=max(A for(A,B)in B);E=min(A for(B,A)in B);F=max(A for(B,A)in B);I=D-C+1;J=F-E+1
			if I>2 and J>2 and len(B)==2*(I+J)-4:
				G=I*J
				if G>M:M,G,S,T,U,V=G,G,C,D,E,F
	C,D,E,F=S,T,U,V;W=next(A[B][G]for B in range(K)for G in range(L)if A[B][G]and not(C<=B<=D and E<=G<=F));H=[A[B][E:F+1]for B in range(C,D+1)];N,O=len(H),len(H[0])
	for P in range(N):
		for Q in range(O):
			if not P*(N-1)*Q*(O-1):H[P][Q]=W
	return H