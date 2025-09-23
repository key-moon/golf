def p(j,A=enumerate):
	for(D,F)in A(j):
		for(B,C)in A(F):
			if C and C^4:
				j[D+1][B]=C
				for E in range(D+1):j[E][B&1::2]=[4]*len(j[E][B&1::2])
				return j