def p(A):
	F=len(A);B=len({*sum(A,[])})-1;D=[[0]*F*B for A in range(F*B)]
	for(C,J)in enumerate(A):
		for(E,H)in enumerate(J):
			if H:
				for G in range(B):D[C*B+G][E*B:E*B+B]=[H]*B
	for I in range(F):
		for G in range(B):
			C=I*B+G
			if not D[C][C]:D[C][C]=2
			E=(F-1-I)*B+B-1-G
			if not D[C][E]:D[C][E]=2
	return D