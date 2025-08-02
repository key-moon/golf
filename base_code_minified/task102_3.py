def p(A):
	F=len(A);G=len(A[0])
	for B in range(F):
		for D in range(B+2,F):
			for C in range(G):
				for E in range(C+2,G):
					if all(A[B][C]==5 for C in range(C,E+1))and all(A[D][B]==5 for B in range(C,E+1))and all(A[B][C]==5 for B in range(B,D+1))and all(A[B][E]==5 for B in range(B,D+1))and all(A[B][D]==0 for B in range(B+1,D)for D in range(C+1,E)):
						for H in range(B+1,D):
							for I in range(C+1,E):A[H][I]=2
	return A