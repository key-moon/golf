r=range(9)
E=lambda	g:[*filter(max,zip(*g))]*3
def	p(g):p=E(E(g));return[[p[i][j]*(0<p[i//3][j//3])for	j	in	r]for	i	in	r]