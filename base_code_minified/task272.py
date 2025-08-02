def p(g):
	for(C,B)in enumerate(g):
		for(A,D)in enumerate(B):
			if D==2 and not(C and g[C-1][A]==2 or C<len(g)-1 and g[C+1][A]==2 or A and B[A-1]==2 or A<len(B)-1 and B[A+1]==2):B[A]=1
	return g