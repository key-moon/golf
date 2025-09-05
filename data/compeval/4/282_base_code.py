def	p(g):
	m,n=len(g),len(g[0]);o=[[0]*n	for	_	in	g]
	for(i,r)in	enumerate(g):
		for(j,v)in	enumerate(r):
			if	v==5:
				for	a	in-1,0,1:
					for	b	in-1,0,1:
						x=i+a
						if	0<=x<m:
							y=j+b
							if	0<=y<n:o[x][y]=5if	a	and	b	else	1if	a	or	b	else	0
	return	o