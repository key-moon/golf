def p(g):
	E,F=len(g),len(g[0]);M=[(A,B)for A in range(E)for B in range(F)if g[A][B]==8];(G,H),(I,J)=M;K,L=(I-G)//abs(I-G),(J-H)//abs(J-H);C,D=-L,K;A,B=G+K,H+L
	while 0<=A-C<E and 0<=B-D<F and g[A-C][B-D]==0:A,B=A-C,B-D
	while 0<=A<E and 0<=B<F and g[A][B]==0:g[A][B]=3;A,B=A+C,B+D
	return g