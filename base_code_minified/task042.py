def p(A):
	for B in range(9):
		for C in range(9):
			if A[B][C]==3:
				if A[B+1][C+1]==3:A[B+2][C-1]=8;A[B-1][C+2]=8
				if A[B+1][C-1]==3:A[B-1][C-2]=8;A[B+2][C+1]=8
	return A