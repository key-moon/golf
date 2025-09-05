def	p(g):
	for	c	in{x	for	r	in	g	for	x	in	r	if	x}:
		l=[(i,j)for(i,r)in	enumerate(g)for(j,x)in	enumerate(r)if	x==c];a,b=zip(*l)
		if	len(l)!=(max(a)-min(a)+1)*(max(b)-min(b)+1):return[[c]]