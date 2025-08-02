def p(g):
	for B in g:
		C=len(B)
		for D in range(C-1,-1,-1):
			if B[D]:break
		A=B[:D+1]
		for E in range(1,len(A)+1):
			if all(A[B]==A[B%E]for B in range(len(A))):break
		B[:]=[A[B%E]for B in range(C)]
	return g