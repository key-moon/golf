A=range(9)
B=lambda	g:[*filter(max,zip(*g))]*3
def	p(g):p=B(B(g));return[[p[i][j]*(0<p[i//3][j//3])for	j	in	A]for	i	in	A]