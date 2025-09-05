def	p(j):
	A=range;c,E=len(j),len(j[0]);k=set();F=[e[:]for	e	in	j]
	def	G(l,J):
		if(l,J)in	k	or	not(0<=l<c	and	0<=J<E)or	j[l][J]!=1:return[]
		k.add((l,J));return[(l,J)]+sum([G(l+e,J+A)for(e,A)in[(-1,0),(1,0),(0,-1),(0,1)]],[])
	for	a	in	A(c):
		for	B	in	A(E):
			if	j[a][B]==1and(a,B)not	in	k:
				e=G(a,B);C,w,D,b=min(e[0]for	e	in	e),max(e[0]for	e	in	e),min(e[1]for	e	in	e),max(e[1]for	e	in	e)
				if	len(e)==2*(w-C+b-D)and	w>C	and	b>D	and	any(j[e][k]==0for	e	in	A(C+1,w)for	k	in	A(D+1,b)):
					for(d,f)in	e:F[d][f]=3
	return	F