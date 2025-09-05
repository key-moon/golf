def	p(j):
	A=range
	for	c	in	A(3):
		for	B	in	A(3):
			if	sum(j[c*4+C][B*4+l]==0for	C	in	A(3)for	l	in	A(3))==5:
				k=[[5if	i%4==3or	j%4==3else	0for	j	in	A(11)]for	i	in	A(11)]
				for	C	in	A(3):
					for	l	in	A(3):
						D=j[c*4+C][B*4+l]
						if	D:
							for	a	in	A(3):
								for	E	in	A(3):k[C*4+a][l*4+E]=D
				return	k