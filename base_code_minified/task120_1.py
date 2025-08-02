def p(A):
	for B in{*sum(A,[])}-{0}:
		C,D=min(A for(A,C)in enumerate(A)for D in C if D==B),max(A for(A,C)in enumerate(A)for D in C if D==B);E,F=min(C for A in A for(C,D)in enumerate(A)if D==B),max(C for A in A for(C,D)in enumerate(A)if D==B)
		for G in range(C+1,D):
			for H in range(E+1,F):A[G][H]=8
	return A