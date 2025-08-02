def p(g):
	G={}
	for(C,P)in enumerate(g):
		for(D,H)in enumerate(P):
			if H:G.setdefault(H,[]).append((C,D))
	(I,A),(J,K)=G.items()
	if A[0][0]==A[1][0]:L=I;E=A[0][0];M=J;F=K[0][1]
	else:L=J;E=K[0][0];M=I;F=A[0][1]
	N,O=len(g),len(g[0]);B=[[0]*O for A in range(N)]
	for C in range(N):B[C][F]=M
	for D in range(O):B[E][D]=L
	B[E][F]=4;return B