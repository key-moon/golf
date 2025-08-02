def p(A):
	B=[]
	for(D,G)in enumerate(A):
		for(E,C)in enumerate(G):
			if C==5:F=D,E
			elif C:B.append((D,E,C))
	H,I=min(A for(A,B,B)in B),max(A for(A,B,B)in B);J,K=min(B for(A,B,A)in B),max(B for(A,B,A)in B);L,M=(H+I)//2,(J+K)//2;N,O=F[0]-L,F[1]-M;A[F[0]][F[1]]=0
	for(D,E,C)in B:A[D+N][E+O]=C
	return A