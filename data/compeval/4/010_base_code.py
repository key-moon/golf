def	p(g):
	d={}
	for	r	in	g:
		for(c,v)in	enumerate(r):
			if	v==5and	c	not	in	d:d[c]=len(d)+1
	return[[d[c]if	v==5else	0for(c,v)in	enumerate(r)]for	r	in	g]