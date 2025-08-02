def p(g):
	J=len(g);G=J-1;A=[A[:]for A in g]
	for(B,K)in enumerate(g):
		for(C,F)in enumerate(K):
			if F:
				D,E=G-B,G-C
				if F%2:
					if C<E:
						for H in range(C,E+1,2):A[B][H]=max(A[B][H],F)
					if B<D:
						for I in range(B,D+1,2):A[I][C]=max(A[I][C],F)
				else:A[B][C]=A[D][C]=A[B][E]=A[D][E]=max(F,A[B][C],A[D][C],A[B][E],A[D][E])
	return A