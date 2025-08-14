def	p(g):
	d={}
	for	x	in	sum(g,[]):d[x]=d.get(x,0)+1
	a=sorted(d.items(),key=lambda	x:(-x[1],x[0]));return[[k	if	c>i	else	0for(k,c)in	a]for	i	in	range(a[0][1])]