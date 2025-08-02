def p(val_g):
	A=val_g
	for B in range(len(A)-1):
		for C in range(len(A[0])-1):
			if A[B][C]==A[B][C+1]==A[B+1][C]==A[B+1][C+1]==0:A[B][C]=A[B][C+1]=A[B+1][C]=A[B+1][C+1]=2
	return A