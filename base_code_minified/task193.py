def p(A):
	H,G=len(A),len(A[0]);D=max(map(max,A));I=[[0]*G for A in A]
	for B in range(H):
		for E in range(B,H):
			for C in range(G):
				for F in range(C,G):
					if all(A[B][E]==D for B in range(B,E+1)for E in range(C,F+1)):
						if not(B and all(A[B-1][C]==D for C in range(C,F+1))or E<H-1 and all(A[E+1][B]==D for B in range(C,F+1))or C and all(A[B][C-1]==D for B in range(B,E+1))or F<G-1 and all(A[B][F+1]==D for B in range(B,E+1))):
							for J in range(B,E+1):
								for K in range(C,F+1):I[J][K]=D
	return I