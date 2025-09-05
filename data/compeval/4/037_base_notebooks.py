def	p(j,A=range):
	c,F=len(j),len(j[0]);k,C={},[A[:]for	A	in	j]
	for	l	in	A(c):
		for	D	in	A(F):
			a=j[l][D]
			if	a:k.setdefault(a,[]).append((l,D))
	for	a	in	k:
		(B,e),(E,w)=k[a];G=1if	E>B	else-1;b=1if	w>e	else-1
		for	d	in	A(abs(E-B)+1):C[B+d*G][e+d*b]=a
	return	C