def p(g):
	B={}
	for(C,F)in enumerate(g):
		for(D,E)in enumerate(F):
			if E:A=B.setdefault(E,[C,C,D,D]);A[0]=min(A[0],C);A[1]=max(A[1],C);A[2]=min(A[2],D);A[3]=max(A[3],D)
	G=max(B,key=lambda v:(B[v][1]-B[v][0]+1)*(B[v][3]-B[v][2]+1));return[[G]*2]*2