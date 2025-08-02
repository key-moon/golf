def p(A):
	L,M=len(A),len(A[0]);J={(B,C)for B in range(L)for C in range(M)if A[B][C]==2}
	while J:
		N,O=J.pop();F=G=N;H=I=O;K=[(N,O)]
		while K:
			B,C=K.pop()
			for(D,E)in((B+1,C),(B-1,C),(B,C+1),(B,C-1)):
				if(D,E)in J:
					J.remove((D,E));K.append((D,E))
					if D<F:F=D
					elif D>G:G=D
					if E<H:H=E
					elif E>I:I=E
		if G>F or I>H:
			for B in range(F-1,G+2):
				if 0<=B<L:
					for C in range(H-1,I+2):
						if 0<=C<M and A[B][C]==0 and(B<F or B>G or C<H or C>I):A[B][C]=3
	return A