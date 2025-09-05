def	p(g,E=enumerate):
	A=[[A	for(i,A)in	E(A)]for	A	in	g]
	for(r,B)in	E(g):
		for(c,C)in	E(B):
			if	C==2:
				for	i	in	range(-1,2):
					for	j	in	range(-1,2):
						try:
							if[i,j]!=[0,0]and	r+i>-1and	c+j>-1:A[r+i][c+j]=1
						except:0
	return	A