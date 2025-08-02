def p(g):
	A,B=len(g),len(g[0]);C=g[0];G=next(A for A in range(1,B)if all(C[B]and C[B]==C[B+A]for B in range(B-A)));D=[g[A][0]for A in range(A)];H=next(B for B in range(1,A)if all(D[A]and D[A]==D[A+B]for A in range(A-B)))
	for E in range(A):
		for F in range(B):
			if g[E][F]==0:g[E][F]=g[E%H][F%G]
	return g