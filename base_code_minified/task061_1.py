def p(A):
	C=len(A);D=0
	for B in range(1,C+1):
		if C%B:continue
		for E in range(C//B):
			for F in range(C//B):
				if all(A[E*B+C][F*B+D]for C in range(B)for D in range(B)):I=[A[F*B:F*B+B]for A in A[E*B:E*B+B]];D=1;break
			if D:break
		if D:break
	for G in range(C):
		for H in range(C):
			if not A[G][H]:A[G][H]=I[G%B][H%B]
	return A