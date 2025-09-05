def	p(j,A=range):
	c,E=len(j),len(j[0]);k,B={},[l[:]for	l	in	j]
	for	l	in	A(c):
		for	C	in	A(E):
			a=j[l][C]
			if	a:k.setdefault(a,[]).append((l,C))
	for	a	in	k:
		(p,D),(e,F)=k[a];w=1if	e>p	else-1;G=1if	F>D	else-1
		for	b	in	A(abs(e-p)+1):B[p+b*w][D+b*G]=a
	return	B