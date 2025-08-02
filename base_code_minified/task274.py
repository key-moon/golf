def p(g):
	C,J=len(g),len(g[0]);D=[A for A in range(C)if 5 in g[A]];E=[A for A in range(J)if any(g[B][A]==5 for B in range(C))];K,L=min(D),max(D);M,N=min(E),max(E);F=[g[A][M+1:N]for A in range(K+1,L)];A=[(A,C)for(A,B)in enumerate(F)for(C,D)in enumerate(B)if D==8]
	if not A:return[[0]*3 for A in range(3)]
	O,P=min(A for(A,B)in A),max(A for(A,B)in A);Q,R=min(A for(B,A)in A),max(A for(B,A)in A);B=[A[Q:R+1]for A in F[O:P+1]];S,T=len(B),len(B[0]);G=[[0]*3 for A in range(3)]
	for H in range(3):
		for I in range(3):
			if B[int(H*S/3)][int(I*T/3)]==8:G[H][I]=8
	return G