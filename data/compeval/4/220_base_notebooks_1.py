def	p(g):
	d={8:4,2:1,3:6};A=enumerate;B=[[A	for(i,A)in	A(B)]for	B	in	g]
	for(r,D)in	A(g):
		for(c,C)in	A(D):
			if	C>0:
				for	i	in	range(-1,2):
					for	j	in	range(-1,2):
						try:
							if[i,j]!=[0,0]:B[r+i][c+j]=d[C]
						except:pass
	return	B