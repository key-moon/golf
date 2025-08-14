def	p(g):
	a,b,c=g;t=6,4,0,0,0,1,3,1,0,0,0,4
	for	i	in	range(len(a)):
		o=t[i%12]
		if	o&1:a[i]=4
		if	o&2:b[i]=4
		if	o&4:c[i]=4
	return	g