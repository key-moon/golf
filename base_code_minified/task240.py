def p(A):
	K=len(A);H=K-1;B=[A[:]for A in A]
	for(C,L)in enumerate(A):
		for(D,G)in enumerate(L):
			if G:
				E,F=H-C,H-D
				if G%2:
					if D<F:
						for I in range(D,F+1,2):B[C][I]=max(B[C][I],G)
					if C<E:
						for J in range(C,E+1,2):B[J][D]=max(B[J][D],G)
				else:B[C][D]=B[E][D]=B[C][F]=B[E][F]=max(G,B[C][D],B[E][D],B[C][F],B[E][F])
	return B