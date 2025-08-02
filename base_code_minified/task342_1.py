def p(A):
	B,C=next((B,C)for B in range(9)for C in range(9)if A[B][C]==A[B][C+1]==A[B+1][C]==A[B+1][C+1]==8);D=[[0]*10 for A in A]
	for E in range(10):
		for F in range(10):
			G=A[E][F]
			if G&7:D[B+(E>B)][C+(F>C)]=G
	return D