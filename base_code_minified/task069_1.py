def p(g):
	A=[(B,D,A)for(B,C)in enumerate(g)for(D,A)in enumerate(C)if A and A!=8]
	if not A:return g
	B=min(A for(A,B,C)in A);C=min(A for(B,A,C)in A);D=[(A-B,D-C,E)for(A,D,E)in A];E=[(B,A)for(B,C)in enumerate(g)for(A,D)in enumerate(C)if D==8 and(B==0 or g[B-1][A]!=8)and(A==0 or C[A-1]!=8)]
	for(F,G)in enumerate(g):g[F]=[0]*len(G)
	for(H,I)in E:
		for(J,K,L)in D:g[H+J][I+K]=L
	return g