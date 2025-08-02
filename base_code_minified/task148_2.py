def p(A):
	B=[A[:]for A in A];F=len(A);G=len(A[0]);H=min(A for C in range(F)for A in range(G)if B[C][A]==2);I=max(A for C in range(F)for A in range(G)if B[C][A]==2);J=set()
	for C in range(F):
		for D in range(G):
			if B[C][D]==8:
				if any(B[C][A]==2 for A in range(D)):
					K=max(A for A in range(D)if B[C][A]==2);J.add(H)
					for E in range(K+1,D):A[C][E]=8
				else:
					K=min(A for A in range(D+1,G)if B[C][A]==2);J.add(I)
					for E in range(D+1,K):A[C][E]=8
				A[C][D]=4
	for L in(H,I):
		if L not in J:
			M=[A for A in range(F)if B[A][L]==2];N=(min(M)+max(M))//2
			if L==H:
				for E in range(H+1,I):A[N][E]=8
			else:
				for E in range(I):A[N][E]=8
	return A