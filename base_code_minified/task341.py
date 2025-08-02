def p(A):
	E={}
	for(B,K)in enumerate(A):
		for(C,D)in enumerate(K):
			if D and D^8:
				if D in E:F,G,H,I=E[D];E[D]=[min(F,B),max(G,B),min(H,C),max(I,C)]
				else:E[D]=[B,B,C,C]
	(F,G,H,I),(L,M,N,O)=E.values();J=lambda A,B,C,B:range(max(A,C)+1,min(B,B))or range(B+1,C)or range(B+1,A)
	for B in J(F,G,L,M):
		for C in J(H,I,N,O):A[B][C]=8
	return A