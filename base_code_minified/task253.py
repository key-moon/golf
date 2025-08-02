def p(g):
	D={}
	for(B,I)in enumerate(g):
		for(C,E)in enumerate(I):
			if E:D.setdefault(E,[]).append((B,C))
	F=[[0]*4 for A in[0]*4]
	for(J,A)in D.items():
		G=min(A for(A,B)in A);H=min(A for(B,A)in A);K=sum(A for(A,B)in A);L=sum(A for(B,A)in A);M=K-1-3*G;N=L-1-3*H
		for(B,C)in A:F[M*2+B-G][N*2+C-H]=J
	return F