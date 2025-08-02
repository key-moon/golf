def p(A):
	I=[(B,C)for B in range(len(A))for C in range(len(A[0]))if A[B][C]];J,K=max(((B,C)for B in I for C in I if A[B[0]][B[1]]!=A[C[0]][C[1]]),key=lambda I:abs(I[0][0]-I[1][0])+abs(I[0][1]-I[1][1]));B,C=D,E=J[0],J[1];D,E=K[0],K[1];F,G=abs(D-B),abs(E-C);M=1 if B<D else-1;N=1 if C<E else-1;H=F-G
	while True:
		if A[B][C]==0:A[B][C]=3
		if B==D and C==E:break
		L=H*2
		if L>-G:H-=G;B+=M
		if L<F:H+=F;C+=N
	return A