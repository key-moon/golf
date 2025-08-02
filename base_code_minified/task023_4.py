def p(A):
	B=[(B,C)for B in range(len(A))for C in range(len(A[0]))if A[B][C]==5]
	if not B:return A
	C=min(A for(A,B)in B);D=min(A for(B,A)in B);E=sum(1 for(A,B)in B if B-D<=A-C);H=len(B)-E;I,J=(2,8)if H>E else(8,2)
	for(F,G)in B:A[F][G]=I if G-D<=F-C else J
	return A