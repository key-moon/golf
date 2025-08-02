def p(val_g):
	B=val_g;C=len(B);D=0
	for A in range(1,C+1):
		if C%A:continue
		for E in range(C//A):
			for F in range(C//A):
				if all(B[E*A+C][F*A+D]for C in range(A)for D in range(A)):I=[B[F*A:F*A+A]for B in B[E*A:E*A+A]];D=1;break
			if D:break
		if D:break
	for G in range(C):
		for H in range(C):
			if not B[G][H]:B[G][H]=I[G%A][H%A]
	return B