def p(A):
	for B in range(len(A)-2):
		for C in range(len(A)-2):
			if sum(A[B+D][C+E]==4 for D in range(3)for E in range(3))==6:
				for D in range(3):
					for E in range(3):
						if not A[B+D][C+E]:A[B+D][C+E]=7
	return A