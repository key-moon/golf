def	p(j,A=len,c=range):
	C,k=A(j),A(j[0])
	for	B	in	c(C):
		if	j[B][0]==2or	j[B][-1]==2:
			for	l	in	c(k):
				if	j[B][l]==0:j[B][l]=2
				elif	j[B][l]!=2:j[B][l]=4
	for	l	in	c(k):
		if	j[0][l]==8or	j[-1][l]==8:
			for	B	in	c(C):
				if	j[B][l]==0:j[B][l]=8
				elif	j[B][l]!=8:j[B][l]=4
	return	j