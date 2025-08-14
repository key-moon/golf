A=range
def	p(g):
	for	i	in	A(64):
		i%=8
		for	j	in	A(i,15-i):g[18-i][j]|=g[i][j];g[j+3][i]|=g[j+1][i]
		if	i<1:*g,=map(list,zip(*g[::-1]))
	return	g