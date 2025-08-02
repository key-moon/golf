def p(A):
	K={A for B in A for A in B if A};B,H=K;M=[(-1,-1),(-1,1),(1,-1),(1,1)];C=lambda L:max(sum((B+C,A+D)in A for(C,D)in M)for(B,A)in L);D=[(A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B];E=[(A,C)for(A,B)in enumerate(A)for(C,D)in enumerate(B)if D==H]
	if C(D)>C(E):F,L=E,B
	else:F,L=D,G=H=B and B
	if C(D)>C(E):F=D;G=H
	else:F=E;G=B
	I=[(A,C)for(A,B)in enumerate(A)for(C,D)in enumerate(B)if D==G];N=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)];J=max(I,key=lambda V:sum((V[0]+A,V[1]+B)in I for(A,B)in N));O=[(A-J[0],B-J[1])for(A,B)in I]
	for(P,Q)in F:
		for(R,S)in O:A[P+R][Q+S]=G
	return A