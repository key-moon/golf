def	p(g):
	A=enumerate;B=[[A	for(i,A)in	A(B)]for	B	in	g]
	for(r,C)in	A(g):
		for(c,D)in	A(C):
			if	D==2:
				for	i	in	range(-1,2):
					for	j	in	range(-1,2):
						try:
							if[i,j]!=[0,0]and	r+i>-1and	c+j>-1:B[r+i][c+j]=1
						except:pass
	return	B