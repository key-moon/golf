def p(A):
	D,G=len(A),len(A[0])
	for C in range(D,0,-1):
		if C&1:
			for E in range(D-C+1):
				for F in range(G-C+1):
					B=[A[F:F+C]for A in A[E:E+C]]
					if len({*sum(B,[])})>1 and B==[A[::-1]for A in B]and B==B[::-1]:return B
	return A