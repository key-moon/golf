def p(A):
	for B in A:
		C=[A for(A,B)in enumerate(B)if B]
		if C:
			E,F=C;G=sum(C)//2
			for D in range(E+1,F):B[D]=[B[E],5,B[F]][(D>G)+(D>=G)]
	return A