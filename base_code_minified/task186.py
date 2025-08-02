def p(A):
	B=sum(sum(A,[]));C=min(B,3);D=[[2]*C+[0]*(3-C)]+[[0]*3]*2
	if B>3:D[1][1]=2
	return D