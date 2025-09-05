def	p(g):
	for	l	in	range(14):
		for	u	in	range(14):
			if	g[u][l+6]==g[u+6][l]==5:
				for	i	in	range(16):
					for	j	in	range(16):
						if	all(0**g[u+y+1][l+x+1]==0**g[i+y][j+x]for	y	in	range(5)for	x	in	range(5)):
							for	y	in	range(5):
								for	x	in	range(5):g[i+y][j+x]=g[i+y][j+x]and	g[u+y+1][l+x+1]
	return	g