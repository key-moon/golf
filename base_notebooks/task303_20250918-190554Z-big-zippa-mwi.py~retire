def p(j,A=range):
	C,D=len(j),len(j[0])
	for B in A(C):
		if sum(j[B])==0:j[B]=[2]*D
	for E in A(D):
		if all(j[A][E]in[0,2]for A in A(C)):
			for B in A(C):j[B][E]=2
	return j