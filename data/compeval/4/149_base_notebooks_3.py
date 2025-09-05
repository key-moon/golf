def	p(j):
	A=range;c=[[0]*3for	_	in	A(3)]
	for	B	in	A(3):
		for	k	in	A(3):
			C=0
			for	l	in	A(3):
				for	D	in	A(3):
					if	j[B*4+l][k*4+D]==6:C+=1
			c[B][k]=1if	C>=2else	0
	return	c