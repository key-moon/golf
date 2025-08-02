def p(A):
	for(B,K)in enumerate(A):
		for(C,I)in enumerate(K):
			if I==8:D,F=C,B
			if I==2:G,E=C,B
	H=(E>F)-(E<F)
	for B in range(F+H,E+H,H):A[B][D]=4
	J=(G>D)-(G<D)
	for C in range(D+J,G,J):A[E][C]=4
	return A