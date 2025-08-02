def p(g):
	A,B=len(g),len(g[0])
	for E in range(1,A+1):
		if all(not g[A][C]or g[A][C]==g[A%E][C]for A in range(A)for C in range(B)):break
	for F in range(1,B+1):
		if all(not g[A][C]or g[A][C]==g[A][C%F]for A in range(A)for C in range(B)):break
	for C in range(A):
		for D in range(B):
			if not g[C][D]:g[C][D]=g[C%E][D%F]
	return g