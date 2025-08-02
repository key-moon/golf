def p(A):
	for(F,C)in enumerate(A):
		B=[-1]
		for(D,G)in enumerate(C):
			if G==2:B+=[D]
		B+=[len(C)]
		for E in range(len(B)-1):
			if E%3==2*(F<1):
				for D in range(B[E]+1,B[E+1]):C[D]=4
	return A