def p(g):
	E={}
	for(B,F)in enumerate(g):
		for(C,D)in enumerate(F):
			if D:A=E.setdefault(D,[B,B,C,C]);A[0]=min(A[0],B);A[1]=max(A[1],B);A[2]=min(A[2],C);A[3]=max(A[3],C)
	for(D,(G,H,I,J))in E.items():
		for B in range(G,H+1):
			for C in range(I,J+1):g[B][C]=D
	return g