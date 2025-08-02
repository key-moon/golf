def p(A):
	D=len(A);E=len(A[0])
	for C in range(D-2):
		for B in range(E-2):
			if all(A[C+D][B+E]==0 for D in range(3)for E in range(3)):
				for F in range(3):A[C+F][B:B+3]=[1]*3
				return A
	return A