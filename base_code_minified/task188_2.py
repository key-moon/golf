def p(A):
	B=len(A);C=len(A[0])
	for D in range(1,B+1):
		if B%D:continue
		for E in range(1,C+1):
			if C%E:continue
			if all(A[B][F]==A[B%D][F%E]for B in range(B)for F in range(C)):return[A[:E]for A in A[:D]]