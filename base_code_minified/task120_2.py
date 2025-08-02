def p(A):
	H,I=len(A),len(A[0])
	for K in range(H):
		for L in range(I):
			J=A[K][L]
			if J:
				D,E,F,G=H,0,I,0
				for B in range(H):
					for C in range(I):
						if A[B][C]==J:
							if B<D:D=B
							if B>E:E=B
							if C<F:F=C
							if C>G:G=C
				if E-D>1 and G-F>1:
					for B in range(D+1,E):
						for C in range(F+1,G):
							if A[B][C]==0:A[B][C]=8
	return A