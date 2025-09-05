def	p(g,k=range):
	A=[[0for	i	in	k(len(A))]for	A	in	g];B=enumerate;C=[]
	for(r,E)in	B(g):
		for(c,D)in	B(E):
			if	D>0:
				for	i	in	k(-9,10):
					for	j	in	k(-9,10):
						try:
							if	0in[i,j]:
								if[r+i,c+j]in	C:A[r+i][c+j]=2
								else:A[r+i][c+j]=int(D)
								C.append([r+i,c+j])
						except:pass
	return	A