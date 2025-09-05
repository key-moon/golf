def	p(g):
	u=[]
	for	r	in	g:
		r=r[:];s={x	for	x	in	r	if	x!=0}
		for	c	in	s:
			v=[j	for(j,x)in	enumerate(r)if	x==c];l,b=min(v),max(v)
			for	j	in	range(l,b+1):
				if	r[j]==0:r[j]=c
		u.append(r)
	return	u