def p(g):
	D=[(A,B)for A in range(10)for B in range(10)if g[A][B]];H=[A for A in D if not any(abs(A[0]-B[0])+abs(A[1]-B[1])==1 for B in D)];I,A=H;B,C=I;J=g[B][C];K=(A[0]>B)-(A[0]<B);L=(A[1]>C)-(A[1]<C)
	for E in range(-10,10):
		F,G=B+K*E,C+L*E
		if 0<=F<10 and 0<=G<10:g[F][G]=J
	return g