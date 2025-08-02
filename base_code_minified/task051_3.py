def p(g):
	B={};[B.setdefault(E,[]).append((A,D))for(A,C)in enumerate(g)for(D,E)in enumerate(C)];A=[A for(A,B)in B.items()if A and len(B)==1][0];D,C=B[A][0];L=[D for(B,C)in B.items()if B and B!=A for D in C];G,H=zip(*L);I,M,J,K=min(G),max(G),min(H),max(H);N,O=len(g),len(g[0])
	if C==J:
		for E in range(K+1,O):g[D][E]=A
	elif C==K:
		for E in range(J):g[D][E]=A
	elif D==I:
		for F in range(M+1,N):g[F][C]=A
	else:
		for F in range(I):g[F][C]=A
	return g