def p(A):
	I={}
	for(F,D)in enumerate(A):
		for(G,E)in enumerate(D):
			if E:I.setdefault(E,[]).append((F,G))
	B=[0,0,0,0,0,0]
	for(E,C)in I.items():
		J,K=min(A[0]for A in C),max(A[0]for A in C);L,M=min(A[1]for A in C),max(A[1]for A in C);H=(K-J+1)*(M-L+1)
		if H==len(C)and H>B[0]:B=[H,J,L,K,M,E]
	D=[[0]*len(A[0])for B in A]
	for F in range(B[1],B[3]+1):
		for G in range(B[2],B[4]+1):D[F][G]=B[5]
	return D