def	p(g):
	k=[]
	for	r	in	g:
		r=r[:];s={x	for	x	in	r	if	x!=0}
		for	c	in	s:
			n=[j	for(j,x)in	enumerate(r)if	x==c];l,A=min(n),max(n)
			for	j	in	range(l,A+1):
				if	r[j]==0:r[j]=c
		k.append(r)
	return	k