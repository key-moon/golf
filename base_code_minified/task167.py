def p(A):
	if len(set(sum(A,[])))<2:return[[5]*3]+[[0]*3]*2
	B=len({A[0][2],A[1][1],A[2][0]})>len({A[0][0],A[1][1],A[2][2]});return[[5 if C==(A,2-A)[B]else 0 for C in range(3)]for A in range(3)]