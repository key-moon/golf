def	p(g):
	A=[]
	for	r	in	g:
		r=r[:];s={x	for	x	in	r	if	x!=0}
		for	c	in	s:
			B=[j	for(j,x)in	enumerate(r)if	x==c];l,C=min(B),max(B)
			for	j	in	range(l,C+1):
				if	r[j]==0:r[j]=c
		A.append(r)
	return	A