def p(A):
	for C in A:
		D=len(C)
		for E in range(D-1,-1,-1):
			if C[E]:break
		B=C[:E+1]
		for F in range(1,len(B)+1):
			if all(B[A]==B[A%F]for A in range(len(B))):break
		C[:]=[B[A%F]for A in range(D)]
	return A