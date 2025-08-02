def p(A):
	F,G=len(A),len(A[0]);J=[(B,C)for B in range(F)for C in range(G)if A[B][C]==2];K=[(B,C)for B in range(F)for C in range(G)if A[B][C]==3];B=min(K,key=lambda I:min(abs(I[0]-A[0])+abs(I[1]-A[1])for A in J));E=min(J,key=lambda J:abs(J[0]-B[0])+abs(J[1]-B[1]));H=(E[0]>B[0])-(E[0]<B[0]);I=(E[1]>B[1])-(E[1]<B[1]);C,D=B
	while 0<=C+H<F and A[C+H][D]!=8:C+=H;A[C][D]=3
	while 0<=D+I<G and A[C][D+I]!=8:D+=I;A[C][D]=3
	return A