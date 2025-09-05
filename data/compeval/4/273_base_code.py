def	p(g):
	for(i,r)in	enumerate(g):
		for	x	in	range(len(r)):
			if	r[x]==4:
				for	y	in	range(x+1,len(r)):
					if	r[y]==4:
						for	k	in	range(i+1,len(g)):
							if	g[k][x]+g[k][y]==8:
								for	a	in	range(i+1,k):
									for	b	in	range(x+1,y):g[a][b]=2
	return	g