def	p(g):
	n,m=len(g),len(g[0])
	for	i	in	range(n):
		for	j	in	range(m):
			if	g[i][j]==2:
				for	a	in-1,0,1:
					for	b	in-1,0,1:
						x,y=i+a,j+b
						if	0<=x<n	and	0<=y<m	and	g[x][y]==0:g[x][y]=1
	return	g