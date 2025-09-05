from	itertools	import	product
def	p(g,O=range):
	for(y,x)in	product(O(len(g)-2),O(len(g[0])-2)):
		A=O(y,y+3)
		if	not	all(4in	i	for	i	in[g[y][x:x+3],g[y+2][x:x+3],[g[a][x]for	a	in	A],[g[a][x+2]for	a	in	A]]):continue
		for(a,b)in	product(A,O(x,x+3)):g[a][b]+=7*(g[a][b]==0)
	return	g