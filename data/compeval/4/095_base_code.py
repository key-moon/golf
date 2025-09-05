def	p(g):
	for(i,a)in	enumerate(g):
		for(j,b)in	enumerate(a):
			if	b==5:
				for	d	in	1,0,-1:
					for	e	in	1,0,-1:
						try:g[i+d][j+e]=g[i+d][j+e]or	1
						except:0
	return	g