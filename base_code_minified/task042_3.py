def p(val_g):
	A=val_g;D,E=len(A),len(A[0]);F=list(map(list,zip(*A[::-1])));G=list(map(list,zip(*A)))[::-1]
	for B in range(D):
		for C in range(E):
			if not A[B][C]and F[B][C]==3 and G[B][C]==3:A[B][C]=8
	return A