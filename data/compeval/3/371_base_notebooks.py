def	p(g):
	A=range;n,m=len(g),len(g[0]);r=[x[:]for	x	in	g];o=[(i,j)for	i	in	A(n)for	j	in	A(m)if	g[i][j]==1];x,y=(o[0][0]+o[1][0])//2,(o[0][1]+o[1][1])//2
	for(a,b)in[(0,0),(-1,0),(1,0),(0,-1),(0,1)]:r[x+a][y+b]=3
	return	r