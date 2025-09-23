def p(j):
	A=3;B=[]
	for D in zip(*j):
		for C in D:
			if C:B+=[C];break
	B+=[0]*(A*A-len(B));return[B[C*A:C*A+A][::1-2*(C%2)]for C in range(A)]