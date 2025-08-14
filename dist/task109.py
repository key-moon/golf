A=range
def	p(g):
	m=len(g)//2;s=2*m;c=g[m][m];r=[[0]*s	for	_	in[0]*s]
	for	y	in	A(m):
		for	x	in	A(m):
			if	g[y][x]:i=s-1-y;j=s-1-x;r[y][x]=r[y][j]=r[i][x]=r[i][j]=c
	return	r