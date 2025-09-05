def	p(g):
	A=range;h,w=len(g),len(g[0]);r=[[g[i][j]for	j	in	A(w)]for	i	in	A(h)]
	for	i	in	A(h):
		for	j	in	A(w):
			if	g[i][j]==2:
				if	j+1<w	and	g[i][j+1]==2and(j<1or	g[i][j-1]!=2)and(j>w-3or	g[i][j+2]!=2):
					for	a	in	A(-1,2):
						for	b	in	A(-1,3):
							x,y=i+a,j+b
							if	0<=x<h	and	0<=y<w	and	r[x][y]==0:r[x][y]=3
				if	i+1<h	and	g[i+1][j]==2and(i<1or	g[i-1][j]!=2)and(i>h-3or	g[i+2][j]!=2):
					for	a	in	A(-1,3):
						for	b	in	A(-1,2):
							x,y=i+a,j+b
							if	0<=x<h	and	0<=y<w	and	r[x][y]==0:r[x][y]=3
	return	r