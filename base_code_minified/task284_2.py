def p(A):
	O=[(B,C,A[B][C])for B in range(len(A))for C in range(len(A[0]))if A[B][C]];(B,C,K),(D,E,L)=O;F=(D>B)-(D<B);H=(E>C)-(E<C);G=(abs(D-B)+abs(E-C))//2;P,Q=B+F*G,C+H*G;R,S=D-F*G,E-H*G
	for I in range(G+1):A[B+F*I][C+H*I]=K;A[D-F*I][E-H*I]=L
	M,N=(0,1)if F else(1,0)
	for J in range(-2,3):A[P+M*J][Q+N*J]=K;A[R+M*J][S+N*J]=L
	return A