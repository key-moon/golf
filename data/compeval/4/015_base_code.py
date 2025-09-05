def	p(g):
	for	i	in	range(9):
		for	j	in	range(9):
			if	g[i][j]==2:
				for(x,y)in(-1,-1),(-1,1),(1,-1),(1,1):
					A=i+x;B=j+y
					if	0<=A<9and	0<=B<9:g[A][B]=4
			if	g[i][j]==1:
				for(x,y)in(-1,0),(1,0),(0,-1),(0,1):
					A=i+x;B=j+y
					if	0<=A<9and	0<=B<9:g[A][B]=7
	return	g