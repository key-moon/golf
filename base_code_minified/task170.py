def p(A):
	O,P=len(A),len(A[0]);B={}
	for S in A:
		for E in S:
			if E:B[E]=B.get(E,0)+1
	Q=max(B,key=B.get);T=O*P;H=I=B=J=K=F=L=G=T;I=J=F=G=-1
	for C in range(O):
		for D in range(P):
			E=A[C][D]
			if E==Q:H,I,B,J=min(H,C),max(I,C),min(B,D),max(J,D)
			elif E:K,F,L,G=min(K,C),max(F,C),min(L,D),max(G,D)
	M,N=F-K+1,G-L+1;U=(I-H)//(M-1)if M>1 else 0;V=(J-B)//(N-1)if N>1 else 0;R=[A[L:G+1]for A in A[K:F+1]]
	for C in range(M):
		for D in range(N):
			if A[H+U*C][B+V*D]!=Q:R[C][D]=0
	return R