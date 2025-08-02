def p(g):
	F={}
	for(C,G)in enumerate(g):
		for(B,D)in enumerate(G):
			if D:
				if D not in F:F[D]=[0,C,C,B,B]
				A=F[D];A[0]+=1;A[1]=min(A[1],C);A[2]=max(A[2],C);A[3]=min(A[3],B);A[4]=max(A[4],B)
	for(J,A)in F.items():
		if A[0]==(A[2]-A[1]+1)*(A[4]-A[3]+1):break
	for E in F:
		if E!=J:break
	K,L,M,N=A[1:];O=K+L;P=M+N
	for(C,G)in enumerate(g):
		for(B,D)in enumerate(G):
			if D==E:H=O-C;I=P-B;G[B]=E;g[C][I]=E;g[H][B]=E;g[H][I]=E
	return g