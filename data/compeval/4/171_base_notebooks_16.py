def p(j,A=range):
	c=len(j);E=len(j[0]);k=[[0 for W in A(E)]for W in A(c)]
	for W in A(c):
		for l in A(E):
			if W==0 or W==c-1 or l==0 or l==E-1:k[W][l]=8
			else:k[W][l]=0
	return k
