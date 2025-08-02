def p(A):
	D=max(map(max,A))
	for(E,B)in enumerate(A):
		for(C,F)in enumerate(B):B[C]=(E+C)%D+1
	return A