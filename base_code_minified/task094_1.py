def p(A):
	C=0
	for(J,G)in enumerate(A):
		if 1 in G:
			B=G.index(1);L=len(G)-1-G[::-1].index(1)
			if not C:M=J;H=B;I=L;C=1
			else:H=min(H,B);I=max(I,L)
		elif C:
			D=(M+J-1)//2;E=(H+I)//2
			for(B,K)in enumerate(A[D]):
				if K!=1:A[D][B]=6
			for F in A:
				if F[E]!=1:F[E]=6
			C=0
	if C:
		D=(M+J)//2;E=(H+I)//2
		for(B,K)in enumerate(A[D]):
			if K!=1:A[D][B]=6
		for F in A:
			if F[E]!=1:F[E]=6
	return A