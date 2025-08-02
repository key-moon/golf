def p(A):
	E=[A for(A,B)in enumerate(A)for C in B if C==8];F=[B for A in A for(B,C)in enumerate(A)if C==8];G,H=min(E),max(E);I,J=min(F),max(F)
	for(C,K)in enumerate(A):
		for(D,B)in enumerate(K):
			if B%8:
				if D<I:A[C][I]=B
				elif D>J:A[C][J]=B
				elif C<G:A[G][D]=B
				elif C>H:A[H][D]=B
	return A