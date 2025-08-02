def p(g):
	A=sum(sum(g,[]));B=min(A,3);C=[[2]*B+[0]*(3-B)]+[[0]*3]*2
	if A>3:C[1][1]=2
	return C