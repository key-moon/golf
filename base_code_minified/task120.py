def p(A):
	for B in{A for B in A for A in B if A and A^8}:
		C=[A for(A,C)in enumerate(A)for D in C if D==B];D=[C for A in A for(C,D)in enumerate(A)if D==B];G,H=min(C),max(C);I,J=min(D),max(D)
		for E in range(G+1,H):
			for F in range(I+1,J):
				if A[E][F]==B:A[E][F]=8
	return A