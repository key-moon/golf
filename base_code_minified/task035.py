def p(A):
	E=min(A for(A,B)in enumerate(A)for(D,C)in enumerate(B)if C==8);I=max(A for(A,B)in enumerate(A)for(D,C)in enumerate(B)if C==8);F=min(B for A in A for(B,C)in enumerate(A)if C==8);G=max(B for A in A for(B,C)in enumerate(A)if C==8)
	for(H,C)in enumerate(A):
		for(D,B)in enumerate(C):
			if B and B!=8:
				if D<F:C[F]=B
				elif D>G:C[G]=B
				elif H<E:A[E][D]=B
	return A