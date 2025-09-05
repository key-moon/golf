def	p(E,R=range):
	n=len(E);a=[[0for	_	in	R(n)]for	_	in	R(n)]
	for	i	in	R(n):
		for	j	in	R(n):
			if	E[i][j]==5:
				for	x	in	R(max(0,i-1),min(n,i+2)):
					for	y	in	R(max(0,j-1),min(n,j+2)):a[x][y]=1
	return	a