def p(A):
	D=list(zip(*A));D=[A for A in D if 5 not in A];B=[list(A)for A in zip(*D)];G=len(B);H=len(B[0])
	for E in range(G):
		for C in range(H):
			if B[E][C]==0:
				for I in(1,-1):
					F=E+I
					if 0<=F<G and B[F][C]!=0:B[E][C]=B[F][C];break
	return B