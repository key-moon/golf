A=range
def	p(g):s={(i//3,j//3)for	i	in	A(9)for	j	in	A(9)if	g[i][j]==5};return[[((i//3,j//3)in	s)*1for	j	in	A(9)]for	i	in	A(9)]