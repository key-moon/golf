def	p(g,E=enumerate):
	d={8:4,2:1,3:6};A=[[A	for(i,A)in	E(A)]for	A	in	g]
	for(r,C)in	E(g):
		for(c,B)in	E(C):
			if	B:
				for	i	in	range(-1,2):
					for	j	in	range(-1,2):
						try:
							if[i,j]!=[0,0]:A[r+i][c+j]=d[B]
						except:0
	return	A