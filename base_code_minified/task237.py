def p(d):
	D,A=len(d),len(d[0])
	for B in range(D):
		for E in range(A):
			if(F:=d[B][E]):
				for C in range(E,A):d[B][C]=F
				for C in range(B,D):d[C][A-1]=F
	return d