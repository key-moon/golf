def	p(j):
	B=len;c=range;A=[]
	for	k	in	c(B(j[0])):
		if	any(j[c][k]==5for	c	in	c(B(j))):A.append(k)
	C=[]
	for	l	in	c(B(j)):
		if	j[l][A[0]]==5:C.append(l)
	D,a=min(C)-1,max(C)+1;E,e=A[0],A[1];return[[j[A][c]for	c	in	c(E,e+1)]for	A	in	c(D,a+1)]