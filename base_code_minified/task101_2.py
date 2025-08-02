def p(g):
	R=len(g);S=len(g[0]);A=[(B,D,A)for(B,C)in enumerate(g)for(D,A)in enumerate(C)if A];B=[(A,B)for(A,B,C)in A if C==2];(C,D),(E,F)=min(B),max(B);G,H=min(A for(A,B,C)in A),min(A for(B,A,C)in A);I=E-C;J=F-D;K=I//(max(A for(A,B,C)in A)-min(A for(A,B,C)in A));L=J//(max(A for(B,A,C)in A)-min(A for(B,A,C)in A))
	for(M,N,O)in A:
		for P in range(1,K+1):
			for Q in range(1,L+1):g[C+P*(M-G)][D+Q*(N-H)]=O
	return g