def	p(g):
	A=range
	for	a	in	A(3):
		for	b	in	A(3):
			if	sum(g[a*4+r][b*4+c]==0for	r	in	A(3)for	c	in	A(3))==5:
				s=[[5if	i%4==3or	j%4==3else	0for	j	in	A(11)]for	i	in	A(11)]
				for	r	in	A(3):
					for	c	in	A(3):
						v=g[a*4+r][b*4+c]
						if	v:
							for	x	in	A(3):
								for	y	in	A(3):s[r*4+x][c*4+y]=v
				return	s