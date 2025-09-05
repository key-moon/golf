def	p(j):
	A=range;c=[e[:]for	e	in	j];D,k=len(j),len(j[0]);F=[(e,l)for	e	in	A(D)for	l	in	A(k)if	j[e][l]==8]
	for(l,B)in	F:
		for(a,C)in[(0,1),(1,0),(0,-1),(-1,0)]:
			e=1
			while	0<=l+e*a<D	and	0<=B+e*C<k:
				if	j[l+e*a][B+e*C]==8:
					for	E	in	A(1,e):c[l+E*a][B+E*C]=3
					break
				e+=1
	return	c