L=len
R=range
def	p(g):
	A=[[0,0,0]for	_	in	R(3)];h,w=L(g),L(g[0])
	for	r	in	R(h):
		for	c	in	R(w):
			if	g[r][c]==5:
				for	i	in	R(-1,2):
					for	j	in	R(-1,2):
						if	r+i>=0and	c+j>=0and	g[r+i][c+j]!=0:A[1+i][1+j]=g[r+i][c+j]
	return	A