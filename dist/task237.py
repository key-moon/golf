A=range
def	p(d):
	n,m=len(d),len(d[0])
	for	i	in	A(n):
		for	j	in	A(m):
			if	f:=d[i][j]:
				for	k	in	A(j,m):d[i][k]=f
				for	k	in	A(i,n):d[k][m-1]=f
	return	d