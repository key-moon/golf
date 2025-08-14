def	p(g):
	a=[[0]*3,[0]*3,[0]*3]
	for	i	in	range(16):y,x=i//8%2*-2+i//2%2,i//4%2*-2+i%2;a[y][x]=max(a[y][x],g[y][x])
	return	a