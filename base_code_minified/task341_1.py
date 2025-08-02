def p(A):
	E={}
	for(C,J)in enumerate(A):
		for(D,F)in enumerate(J):
			if F:B=E.setdefault(F,[C,C,D,D]);B[0]=min(B[0],C);B[1]=max(B[1],C);B[2]=min(B[2],D);B[3]=max(B[3],D)
	G,H=E.values();I=lambda H,I,c,d:range(I+1,c)if I<c else range(d+1,H)if d<H else range(max(H,c)+1,min(I,d))
	for C in I(*G[:2],*H[:2]):
		for D in I(*G[2:],*H[2:]):A[C][D]=8
	return A