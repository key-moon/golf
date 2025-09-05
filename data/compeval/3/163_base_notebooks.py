def	p(j):
	A=range
	for	c	in	A(3):
		for	E	in	A(3):
			k=[[j[4*c+B][4*E+l]for	l	in	A(3)]for	B	in	A(3)]
			for	C	in	A(3):
				for	l	in	A(3):
					if	k[C][l]==4:
						B=[[0]*11for	_	in	A(11)]
						for	a	in	A(3):
							for	D	in	A(3):B[4*C+a][4*l+D]=k[a][D]
						for	e	in	A(11):B[e][3]=B[e][7]=B[3][e]=B[7][e]=5
						return	B