def p(A):
	D,E=len(A),len(A[0]);F={}
	for B in range(D):
		for C in range(E):
			L=A[B][C]
			if L:F[L]=F.get(L,0)+1
	G=min(F,key=F.get);H,I=D,E;M,N=-1,-1
	for B in range(D):
		for C in range(E):
			if A[B][C]==G:
				if B<H:H=B
				if B>M:M=B
				if C<I:I=C
				if C>N:N=C
	for O in(H,M):
		for P in(I,N):
			J=-1 if O==H else 1;K=-1 if P==I else 1;B,C=O+J,P+K
			while 0<=B<D and 0<=C<E and A[B][C]in(0,G):B+=J;C+=K
			if 0<=B<D and 0<=C<E and A[B][C]not in(0,G):
				B+=J;C+=K
				while 0<=B<D and 0<=C<E:
					if A[B][C]==0:A[B][C]=G
					B+=J;C+=K
	return A