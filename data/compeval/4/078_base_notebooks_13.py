def	p(j,A=range):
	c,C=len(j),len(j[0]);k=[[0]*C	for	A	in	A(c)]
	for	B	in	A(C):
		l=[j[c][B]for	c	in	A(c)if	j[c][B]!=0]
		for(D,a)in	enumerate(l):k[D][B]=a
	return	k