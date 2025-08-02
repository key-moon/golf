def p(A):
	G={}
	for(D,H)in enumerate(A):
		for(C,E)in enumerate(H):
			if E:
				if E not in G:G[E]=[0,D,D,C,C]
				B=G[E];B[0]+=1;B[1]=min(B[1],D);B[2]=max(B[2],D);B[3]=min(B[3],C);B[4]=max(B[4],C)
	for(K,B)in G.items():
		if B[0]==(B[2]-B[1]+1)*(B[4]-B[3]+1):break
	for F in G:
		if F!=K:break
	L,M,N,O=B[1:];P=L+M;Q=N+O
	for(D,H)in enumerate(A):
		for(C,E)in enumerate(H):
			if E==F:I=P-D;J=Q-C;H[C]=F;A[D][J]=F;A[I][C]=F;A[I][J]=F
	return A