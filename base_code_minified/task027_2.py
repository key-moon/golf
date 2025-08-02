def p(A):
	B,E=len(A),len(A[0]);D=lambda F,G:0<=F<B and 0<=G<E and A[F][G]>0
	while 1:
		C=[(B,C)for B in range(B)for C in range(E)if A[B][C]==0 and(D(B-1,C)and D(B,C-1)or D(B-1,C)and D(B,C+1)or D(B+1,C)and D(B,C-1)or D(B+1,C)and D(B,C+1))]
		if not C:break
		for(F,G)in C:A[F][G]=2
	return A