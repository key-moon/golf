def p(A):
	F,D=len(A),len(A[0]);G,I=[A for(A,B)in enumerate(A)if B==[8]*D];E,H=[B for B in range(D)if[A[B]for A in A]==[8]*F]
	for C in range(F):
		for B in range(D):
			if A[C][B]==0:
				if G<C<I:A[C][B]=6 if E<B<H else 4 if B<E else 3
				elif E<B<H:A[C][B]=2 if C<G else 1
	return A