def p(A):
	F=len(A[0])
	for D in range(F):
		B=-1
		for(C,H)in enumerate(A):
			if H[D]==7:B=C
		if B<0:continue
		for C in range(B,-1,-1):
			for E in range(B-C+1):
				for G in(D+E,D-E):
					if 0<=G<F:A[C][G]=7+(E&1)
	return A