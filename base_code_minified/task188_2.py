def p(g):
	A=len(g);B=len(g[0])
	for C in range(1,A+1):
		if A%C:continue
		for D in range(1,B+1):
			if B%D:continue
			if all(g[A][E]==g[A%C][E%D]for A in range(A)for E in range(B)):return[A[:D]for A in g[:C]]