def p(g):
	N=[(A,B,g[A][B])for A in range(len(g))for B in range(len(g[0]))if g[A][B]];(A,B,J),(C,D,K)=N;E=(C>A)-(C<A);G=(D>B)-(D<B);F=(abs(C-A)+abs(D-B))//2;O,P=A+E*F,B+G*F;Q,R=C-E*F,D-G*F
	for H in range(F+1):g[A+E*H][B+G*H]=J;g[C-E*H][D-G*H]=K
	L,M=(0,1)if E else(1,0)
	for I in range(-2,3):g[O+L*I][P+M*I]=J;g[Q+L*I][R+M*I]=K
	return g