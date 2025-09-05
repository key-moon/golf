def	p(j,A=range):
	c,C=len(j),len(j[0]);k=[0for	A	in	A(C)]
	for	B	in	A(C):
		for	l	in	A(c):
			if	j[l][B]>0:k[B]+=1
			j[l][B]=0
	D=min([A	for	A	in	k	if	A>0]);B=k.index(D)
	for	l	in	A(k[B]):j[-(l+1)][B]=2
	B=k.index(max(k))
	for	l	in	A(k[B]):j[-(l+1)][B]=1
	return	j