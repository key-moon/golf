def p(A):
	D=len(A)
	for E in range(D):
		for F in range(D):
			if not A[E][F]:
				B,C=E,F
				for G in range(3):
					B,C=C,D-1-B
					if A[B][C]:A[E][F]=A[B][C];break
	return A