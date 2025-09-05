def	p(g):
	C=0
	if	len({x	for	x	in	g[0]if	x})>1:g=[list(r)for	r	in	zip(*g)];C=1
	D,E=len(g),len(g[0]);A=0
	while	A<D:
		F=next(x	for	x	in	g[A]if	x);B=A
		while	B<D	and	set(g[B])-{0}=={F}:B+=1
		G={k	for	r	in	range(A,B)for	k	in	range(E)if	g[r][k]==0}
		for	r	in	range(A,B):
			for	k	in	G:g[r][k]=0
		A=B
	if	C:g=[list(r)for	r	in	zip(*g)]
	return	g