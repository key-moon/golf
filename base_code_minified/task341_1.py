def p(g):
	D={}
	for(B,I)in enumerate(g):
		for(C,E)in enumerate(I):
			if E:A=D.setdefault(E,[B,B,C,C]);A[0]=min(A[0],B);A[1]=max(A[1],B);A[2]=min(A[2],C);A[3]=max(A[3],C)
	F,G=D.values();H=lambda a,b,c,d:range(b+1,c)if b<c else range(d+1,a)if d<a else range(max(a,c)+1,min(b,d))
	for B in H(*F[:2],*G[:2]):
		for C in H(*F[2:],*G[2:]):g[B][C]=8
	return g