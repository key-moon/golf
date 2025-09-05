def	p(g,K=enumerate):
	A=[r[:]for	r	in	g]
	for(y,r)in	K(g):
		for(x,v)in	K(r):
			for	i	in-1,0,1:
				for	j	in-1,0,1:
					if	v	and	i|j	and(v==2and	i*j	or	v==1and	not	i*j):
						b=y+i;a=x+j
						if	0<=b<len(g)and	0<=a<len(g[0])and	A[b][a]<1:A[b][a]=4+3*(v&1)
	return	A