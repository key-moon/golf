def	p(j):
	C=range;c=[A[:]for	A	in	j]
	for	A	in	C(len(j)):
		for	k	in	C(len(j[0])):
			if	j[A][k]==2:D,l=A,k
			if	j[A][k]==3:E,a=A,k
	B=1if	a>l	else-1
	for	k	in	C(l+B,a+B,B):c[D][k]=8
	B=1if	E>D	else-1
	for	A	in	C(D+B,E,B):c[A][a]=8
	return	c