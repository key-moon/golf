def p(g):
	A=[A[:]for A in g];M=len(A);S=len(A[0]);H=[B for A in A for(B,C)in enumerate(A)if C==2]
	if not H:return A
	E=min(H);F=max(H);N=[A for(A,B)in enumerate(A)if 2 in B];T=min(N);U=max(N);I=[A for(A,B)in enumerate(A)if all(B[A]==2 for A in range(E,F+1))];V=bool(I)
	if V:
		J=min(I);K=max(I)
		for C in range(J+1,K):
			D=[B for B in range(E+1,F)if A[C][B]==5]
			if not D:continue
			for B in D:A[C][B]=0
			O=C-J;P=K-C
			if O<=P:
				G=J-O
				if 0<=G<M:
					for B in D:A[G][B]=5
			else:
				G=K+P
				if 0<=G<M:
					for B in D:A[G][B]=5
	else:
		for C in range(T,U+1):
			D=[B for B in range(E+1,F)if A[C][B]==5]
			if not D:continue
			for B in D:
				Q=B-E;R=F-B
				if Q<=R:L=E-Q
				else:L=F+R
				if 0<=L<S:A[C][L]=5
				A[C][B]=0
	return A