def	p(g,R=range):
	n=len(g)
	for	i	in	R(n):
		if	g[i][0]==2:
			a=0
			while	a<n	and	g[i][a]==2:a+=1
			for	x	in	R(n):
				for	y	in	R((a+i-x)*(x!=i)):g[x][y]=3-2*(x>i)
	return	g