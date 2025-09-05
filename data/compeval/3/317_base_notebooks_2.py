def	p(R,u=range):
	n=len(R);A=[[0for	_	in	u(n)]for	_	in	u(n)]
	for	i	in	u(n):
		for	j	in	u(n):
			if	R[i][j]==5:
				for	x	in	u(max(0,i-1),min(n,i+2)):
					for	y	in	u(max(0,j-1),min(n,j+2)):A[x][y]=1
	return	A