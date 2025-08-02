def p(A):
	B,C=len(A),len(A[0])
	for F in range(1,B+1):
		if all(not A[B][D]or A[B][D]==A[B%F][D]for B in range(B)for D in range(C)):break
	for G in range(1,C+1):
		if all(not A[B][D]or A[B][D]==A[B][D%G]for B in range(B)for D in range(C)):break
	for D in range(B):
		for E in range(C):
			if not A[D][E]:A[D][E]=A[D%F][E%G]
	return A