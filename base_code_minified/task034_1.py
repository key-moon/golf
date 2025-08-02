def p(A):
	G=len(A);H=len(A[0]);B=[]
	for I in range(G):
		for J in range(H):
			if A[I][J]!=0:B.append((I,J,A[I][J]))
	N=sorted({A for(A,B,B)in B});O=sorted({B for(A,B,A)in B});Y,Z=N[0],N[-1];a,b=O[0],O[-1];P=[A for(*B,A)in B]
	for K in set(P):
		if P.count(K)==1:Q=K
		else:c=K
	d=max(Q,c);C,D=next((A,B)for(A,B,C)in B if C==Q);E,F=Y+Z-C,a+b-D;R=C-E and(C-E)//abs(C-E);S=D-F and(D-F)//abs(D-F);T=S,-R;U=[A[:]for A in A];L,M=E,F
	while 0<=L<G and 0<=M<H:
		for V in(-1,0,1):
			W=L+T[0]*V;X=M+T[1]*V
			if 0<=W<G and 0<=X<H:U[W][X]=d
		L+=R;M+=S
	return U