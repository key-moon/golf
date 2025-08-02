def p(A):
	F,G=len(A),len(A[0]);N=[(B,C)for B in range(F)for C in range(G)if A[B][C]==8];(H,I),(J,K)=N;L,M=(J-H)//abs(J-H),(K-I)//abs(K-I);D,E=-M,L;B,C=H+L,I+M
	while 0<=B-D<F and 0<=C-E<G and A[B-D][C-E]==0:B,C=B-D,C-E
	while 0<=B<F and 0<=C<G and A[B][C]==0:A[B][C]=3;B,C=B+D,C+E
	return A