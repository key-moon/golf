def	p(g):
	z=0;A=enumerate;B=[[A	for(i,A)in	A(B)]for	B	in	g]
	for(r,D)in	A(g):
		for(c,C)in	A(D):
			try:
				if	C!=0and	g[r][c+1]!=0and	g[r][c-1]!=0:
					for	i	in	range(-2,3):
						for	j	in	range(-2,3):
							if	abs(i)==abs(j):B[r+i][c+j]=C
							elif	0in[i,j]:B[r+i][c+j]=g[r][c-1]
			except:pass
	return	B