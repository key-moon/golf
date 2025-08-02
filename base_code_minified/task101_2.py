def p(A):
	S=len(A);T=len(A[0]);B=[(B,D,A)for(B,C)in enumerate(A)for(D,A)in enumerate(C)if A];C=[(A,B)for(A,B,C)in B if C==2];(D,E),(F,G)=min(C),max(C);H,I=min(A for(A,B,C)in B),min(A for(B,A,C)in B);J=F-D;K=G-E;L=J//(max(A for(A,B,C)in B)-min(A for(A,B,C)in B));M=K//(max(A for(B,A,C)in B)-min(A for(B,A,C)in B))
	for(N,O,P)in B:
		for Q in range(1,L+1):
			for R in range(1,M+1):A[D+Q*(N-H)][E+R*(O-I)]=P
	return A