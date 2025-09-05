def	p(j,A=range):
	c,B,k,C=len(j),len(j[0]),0,0
	for	l	in	A(c):
		for	E	in	A(B):
			if	j[l][E]:k,C=l+2,E
	def	s(l,J,a):
		if	0<=J<B:j[l][J]=a
	for	D	in	A(B):
		k,a=k-1,7+D%2
		for	l	in	A(k):s(l,C-D,a);s(l,C+D,a)
	return	j