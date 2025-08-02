def p(g):
	F=len(g);G=len(g[0]);A=[]
	for H in range(F):
		for I in range(G):
			if g[H][I]!=0:A.append((H,I,g[H][I]))
	M=sorted({A for(A,B,B)in A});N=sorted({B for(A,B,A)in A});X,Y=M[0],M[-1];Z,a=N[0],N[-1];O=[A for(*B,A)in A]
	for J in set(O):
		if O.count(J)==1:P=J
		else:b=J
	c=max(P,b);B,C=next((A,B)for(A,B,C)in A if C==P);D,E=X+Y-B,Z+a-C;Q=B-D and(B-D)//abs(B-D);R=C-E and(C-E)//abs(C-E);S=R,-Q;T=[A[:]for A in g];K,L=D,E
	while 0<=K<F and 0<=L<G:
		for U in(-1,0,1):
			V=K+S[0]*U;W=L+S[1]*U
			if 0<=V<F and 0<=W<G:T[V][W]=c
		K+=Q;L+=R
	return T