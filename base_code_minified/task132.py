def p(A):
	F={}
	for(C,G)in enumerate(A):
		for(D,E)in enumerate(G):
			if E:B=F.setdefault(E,[C,C,D,D]);B[0]=min(B[0],C);B[1]=max(B[1],C);B[2]=min(B[2],D);B[3]=max(B[3],D)
	for(E,B)in F.items():
		for C in range(B[0],B[1]+1):
			for D in range(B[2],B[3]+1):A[C][D]=E
	return A