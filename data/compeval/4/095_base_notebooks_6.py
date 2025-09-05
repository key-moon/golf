def	p(g):
	A=enumerate
	for(r,B)in	A(g):
		for(c,C)in	A(B):
			if	C==5:
				for	i	in	range(r-1,r+2):
					for	j	in	range(c-1,c+2):
						if[i,j]!=[r,c]:g[i][j]=1
	return	g