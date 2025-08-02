def p(g):
	B={}
	for(C,G)in enumerate(g):
		for(D,E)in enumerate(G):
			if E:
				A=B.get(E)
				if A:A[0]=min(A[0],C);A[1]=max(A[1],C);A[2]=min(A[2],D);A[3]=max(A[3],D)
				else:B[E]=[C,C,D,D]
	F=min(B,key=lambda x:(B[x][1]-B[x][0]+1)*(B[x][3]-B[x][2]+1));A=B[F];return[[F]*(A[3]-A[2]+1)for B in range(A[1]-A[0]+1)]