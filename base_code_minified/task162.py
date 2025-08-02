def p(A):
	for B in range(len(A)-2):
		for C in range(len(A[0])-2):
			if not sum(sum(A[C:C+3])for A in A[B:B+3]):
				for D in A[B:B+3]:D[C:C+3]=[1]*3
				return A