def p(g):
	D={}
	for(A,J)in enumerate(g):
		for(B,C)in enumerate(J):
			if C and C^8:
				if C in D:E,F,G,H=D[C];D[C]=[min(E,A),max(F,A),min(G,B),max(H,B)]
				else:D[C]=[A,A,B,B]
	(E,F,G,H),(K,L,M,N)=D.values();I=lambda A,B,C,D:range(max(A,C)+1,min(B,D))or range(B+1,C)or range(D+1,A)
	for A in I(E,F,K,L):
		for B in I(G,H,M,N):g[A][B]=8
	return g