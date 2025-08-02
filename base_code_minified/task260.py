def p(A):
	F=len(A);D=max({A for B in A for A in B if A},key=lambda F:sum(A.count(F)for A in A));B=[(B,E)for(B,C)in enumerate(A)for(E,A)in enumerate(C)if A and A!=D]
	if not B:return A
	G=min(A for(A,B)in B);H=max(A for(A,B)in B);I=min(A for(B,A)in B);J=max(A for(B,A)in B)
	for C in range(F):
		for K in range(F):A[C][K]=0
	for E in range(H-G+1):C=G+E;A[C][I+E]=D;A[C][J-E]=D
	return A