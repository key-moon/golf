def	p(g,N=range,E=enumerate):
	A=[[0for	i	in	N(len(b))]for	b	in	g];B=[]
	for(r,D)in	E(g):
		for(c,C)in	E(D):
			if	C>0:
				for	i	in	N(-9,10):
					for	j	in	N(-9,10):
						try:
							if	0in[i,j]:
								if[r+i,c+j]in	B:A[r+i][c+j]=2
								else:A[r+i][c+j]=C
								B+=[[r+i,c+j]]
						except:0
	return	A