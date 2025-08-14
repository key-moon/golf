A=range
def	p(g):
	for	w	in	A(8,16):
		x,y,h=w%4,w//4,len(g)
		if	all(g[i][j]==g[i-y][j-x]for	i	in	A(y,h)for	j	in	A(x,10)):return	g+[[0]*(v:=i//y*x)+g[i%y][:10-v]for	i	in	A(h,10)]