def p(A):
	E,F=len(A),len(A[0])
	for B in range(E):
		for C in range(F):
			if A[B][C]==5:
				for D in range(3,min(E-B,F-C)+1):
					if all(A[B][C+E]==5 and A[B+D-1][C+E]==5 and A[B+E][C]==5 and A[B+E][C+D-1]==5 for E in range(D)):
						for G in range(1,D-1):
							for H in range(1,D-1):
								if A[B+G][C+H]==0:A[B+G][C+H]=2
	return A