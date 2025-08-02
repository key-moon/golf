def p(A):
	E={}
	for(C,M)in enumerate(A):
		for(D,F)in enumerate(M):
			if F:
				B=E.get(F)
				if B:
					if C<B[0]:B[0]=C
					if C>B[1]:B[1]=C
					if D<B[2]:B[2]=D
					if D>B[3]:B[3]=D
				else:E[F]=[C,C,D,D]
	G=0,[]
	for(N,(H,I,J,K))in E.items():
		L=[A[J:K+1]for A in A[H:I+1]]
		if all(A==A[::-1]for A in L)and(I-H+1)*(K-J+1)>G[0]:G=(I-H+1)*(K-J+1),L
	return G[1]