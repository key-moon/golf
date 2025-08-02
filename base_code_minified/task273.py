def p(A):
	for(F,B)in enumerate(A):
		for C in range(len(B)):
			if B[C]==4:
				for D in range(C+1,len(B)):
					if B[D]==4:
						for E in range(F+1,len(A)):
							if A[E][C]+A[E][D]==8:
								for G in range(F+1,E):
									for H in range(C+1,D):A[G][H]=2
	return A