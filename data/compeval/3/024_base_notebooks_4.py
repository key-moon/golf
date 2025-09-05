def	p(g):
	B=[];E=[];C=enumerate
	for(r,A)in	C(g):
		if	1in	A:B.append([1for	_	in	A])
		elif	3in	A:B.append([3for	_	in	A])
		else:B.append(A[:])
		for(c,D)in	C(A):
			if	D==2:E.append(c)
	for(r,A)in	C(B):
		for(c,D)in	C(A):
			if	c	in	E	and	D==0:B[r][c]=2
	return	B