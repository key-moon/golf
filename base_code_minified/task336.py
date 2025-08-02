def p(A):
	I,J=len(A),len(A[0]);F=min(B for B in range(I)for C in range(J)if A[B][C]==5);G=max(B for B in range(I)for C in range(J)if A[B][C]==5);H=min(B for C in range(I)for B in range(J)if A[C][B]==5);K=max(B for C in range(I)for B in range(J)if A[C][B]==5)
	for C in range(H,K+1):
		if A[F][C]==0:D,E=F,C;break
	else:
		for C in range(H,K+1):
			if A[G][C]==0:D,E=G,C;break
		else:
			for B in range(F,G+1):
				if A[B][H]==0:D,E=B,H;break
			else:
				for B in range(F,G+1):
					if A[B][K]==0:D,E=B,K;break
	for B in range(F+1,G):
		for L in range(H+1,K):
			if A[B][L]==0:A[B][L]=8
	if D==F:
		for B in range(D+1):A[B][E]=8
	elif D==G:
		for B in range(D,I):A[B][E]=8
	elif E==H:
		for C in range(E+1):A[D][C]=8
	else:
		for C in range(E,J):A[D][C]=8
	return A