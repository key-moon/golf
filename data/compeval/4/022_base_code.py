def	p(g):
	o=[[0]*3for	_	in[0]*3]
	for(i,r)in	enumerate(g):
		for(j,v)in	enumerate(r):
			if	v==5:
				for	A	in-1,0,1:
					for	B	in-1,0,1:
						if	A|B:
							try:t=g[i+A][j+B]
							except:pass
							else:
								if	t	and	t-5:o[A+1][B+1]=t
	o[1][1]=5;return	o