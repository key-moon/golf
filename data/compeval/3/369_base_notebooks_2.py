def	p(j):
	B=range;c=set();C=[c[:]for	c	in	j]
	def	D(k,W):
		if(k,W)in	c	or	not(0<=k<10and	0<=W<10)or	j[k][W]:return[]
		c.add((k,W));return[(k,W)]+sum([D(k+c,W+l)for(c,l)in[(-1,0),(1,0),(0,-1),(0,1)]],[])
	for	l	in	B(10):
		for	A	in	B(10):
			if	j[l][A]==0and(l,A)not	in	c:
				a=D(l,A)
				for(E,e)in	a:C[E][e]=abs(len(a)-4)
	return	C