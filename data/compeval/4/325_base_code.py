def	p(g):
	A={x+y*1j	for(x,r)in	enumerate(g)for(y,v)in	enumerate(r)if	v};n=0
	while	A:
		w=[A.pop()]
		while	w:
			p=w.pop()
			for	d	in	1,-1,1j,-1j:
				if	p+d	in	A:A.remove(p+d);w.append(p+d)
		n+=1
	return[[8*(i==j)for	j	in	range(n)]for	i	in	range(n)]