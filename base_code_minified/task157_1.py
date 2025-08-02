def p(A):
	C,D=len(A),len(A[0]);B=[(B,C)for B in range(C)for C in range(D)if A[B][C]==5]
	if not B:return A
	G=min(A for(A,B)in B);H=min(A for(B,A)in B);I=max(A for(A,B)in B)-G;J=[(B-H,I-(A-G))for(A,B)in B];K=min(B for B in range(C)for C in range(D)if A[B][C]==2);L=min(B for B in range(D)for D in range(C)if A[D][B]==2)
	for(M,N)in J:
		E,F=K+M,L+N
		if 0<=E<C and 0<=F<D and A[E][F]==0:A[E][F]=1
	return A