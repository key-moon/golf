def	p(g):
	h=len(g)
	for(A,r)in	enumerate(g):
		if	8in	r:B=r.index(8);break
	for(y,r)in	enumerate(g):
		if	y==A:continue
		d=abs(A-y);s=1if	y<A	else-1;p=B+s*d
		if	d&1:
			x=p-s
			if	0<=x<h:r[x]=5
		else:
			for	x	in	range(p-2,p+1)if	y<A	else	range(p,p+3):
				if	0<=x<h:r[x]=5
	return	g