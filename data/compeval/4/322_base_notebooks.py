def	p(j,A=range):
	for	c	in	A(len(j[0])):
		for	B	in	A(len(j)):
			if	j[B][c]:break
		else:continue
		for	k	in	A(B,len(j)):j[k][c]=j[B][c]
	return	j