def p(A):
	B={}
	for(C,N)in enumerate(A):
		for(D,I)in enumerate(N):
			if I:B.setdefault(I,[]).append((C,D))
	E=min(B,key=lambda F:(min(A for(A,B)in B[F]),min(A for(B,A)in B[F])));J,K=min(A for(A,B)in B[E]),min(A for(B,A)in B[E]);F=next(A for A in B if A!=E and min(A for(A,B)in B[A])==J);G=next(A for A in B if A!=E and min(A for(B,A)in B[A])==K);L=min(A for(A,B)in B[G])-J;M=min(A for(B,A)in B[F])-K;O,P=len(A),len(A[0]);Q=(P-1-max(A for(B,A)in B[F]))//M
	for H in range(1,Q+1):
		for(C,D)in B[F]:A[C][D+M*H]=F
	R=(O-1-max(A for(A,B)in B[G]))//L
	for H in range(1,R+1):
		for(C,D)in B[G]:A[C+L*H][D]=G
	return A