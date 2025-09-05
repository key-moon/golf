def	p(g):
	A=range
	for	r	in	A(3):
		for	c	in	A(3):
			b=[[g[4*r+i][4*c+j]for	j	in	A(3)]for	i	in	A(3)]
			for	i	in	A(3):
				for	j	in	A(3):
					if	b[i][j]==4:
						z=[[0]*11for	_	in	A(11)]
						for	x	in	A(3):
							for	y	in	A(3):z[4*i+x][4*j+y]=b[x][y]
						for	k	in	A(11):z[k][3]=z[k][7]=z[3][k]=z[7][k]=5
						return	z