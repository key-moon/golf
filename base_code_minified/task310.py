def p(A):
	for C in range(len(A)-6):
		for B in range(len(A[0])-6):
			D=A[C][B]
			if A[C][B:B+7]==[D]*7==A[C+6][B:B+7]and all(A[C+E][B:B+7:6]==[D,D]for E in range(7)):return[A[B:B+7]for A in A[C:C+7]]