def	p(g):
	z=0;B=enumerate;A=[[A	for(i,A)in	B(A)]for	A	in	g]
	for(r,D)in	B(g):
		for(c,C)in	B(D):
			if	C==2:
				for	i	in	range(-1,2):
					for	j	in	range(-1,2):
						try:
							if	abs(i)==abs(j)and	A[r+i][c+j]==0:A[r+i][c+j]=4
						except:pass
			if	C==1:
				for	i	in	range(-1,2):
					for	j	in	range(-1,2):
						try:
							if	0in[i,j]and	A[r+i][c+j]==0:A[r+i][c+j]=7
						except:pass
	return	A