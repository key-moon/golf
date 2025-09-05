def	p(g):
	A=[]
	for	r	in	g:
		r=r[:];s={x	for	x	in	r	if	x!=0}
		for	c	in	s:
			u=[j	for(j,x)in	enumerate(r)if	x==c];l,B=min(u),max(u)
			for	j	in	range(l,B+1):
				if	r[j]==0:r[j]=c
		A.append(r)
	return	A