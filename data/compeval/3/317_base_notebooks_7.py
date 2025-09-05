def	p(m,F=range):
	n=len(m);A=[[0for	_	in	F(n)]for	_	in	F(n)]
	for	i	in	F(n):
		for	j	in	F(n):
			if	m[i][j]==5:
				for	x	in	F(max(0,i-1),min(n,i+2)):
					for	y	in	F(max(0,j-1),min(n,j+2)):A[x][y]=1
	return	A