def p(A):
	D,E=len(A),len(A[0])
	for F in range(D):
		for G in range(E):
			if A[F][G]==2:
				for H in(-1,0,1):
					for I in(-1,0,1):
						B,C=F+H,G+I
						if 0<=B<D and 0<=C<E and A[B][C]==0:A[B][C]=1
	return A