def p(g):
	E={}
	for(B,F)in enumerate(g):
		for(C,D)in enumerate(F):
			if D:A=E.setdefault(D,[B,B,C,C]);A[0]=min(A[0],B);A[1]=max(A[1],B);A[2]=min(A[2],C);A[3]=max(A[3],C)
	for(D,A)in E.items():
		for B in range(A[0],A[1]+1):
			for C in range(A[2],A[3]+1):g[B][C]=D
	return g