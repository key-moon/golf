def	p(g):
	h=len(g)
	for(i,r)in	enumerate(g):
		for(j,v)in	enumerate(r):
			if	v==5:
				A=[(i,j)];g[i][j]=0
				for(a,b)in	A:
					for	d	in(1,0),(-1,0),(0,1),(0,-1):
						x,y=a+d[0],b+d[1]
						if	0<=x<h	and	0<=y<len(r)and	g[x][y]==5:g[x][y]=0;A+=[(x,y)]
				d=2if	len(A)==6else	1
				for(a,b)in	A:g[a][b]=d
	return	g