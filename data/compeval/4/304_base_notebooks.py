def	p(j,A=range(9),c=range(3)):
	C,k=__import__('collections').Counter(j[0]+j[1]+j[2]).most_common(1)[0][0],[[0for	_	in	A]for	_	in	A]
	for(D,l)in[(A,l)for	l	in	c	for	A	in	c	if	j[A][l]==C]:
		for	B	in	A:k[3*D+B%3][3*l+B//3]=j[B%3][B//3]
	return	k