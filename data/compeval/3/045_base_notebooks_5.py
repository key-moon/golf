def	p(g):
	v=[]
	for	r	in	g:
		r=r[:];s={x	for	x	in	r	if	x!=0}
		for	c	in	s:
			A=[j	for(j,x)in	enumerate(r)if	x==c];l,B=min(A),max(A)
			for	j	in	range(l,B+1):
				if	r[j]==0:r[j]=c
		v.append(r)
	return	v