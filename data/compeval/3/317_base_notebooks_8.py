def	p(j,A=range):
	c=len(j);C=[[0for	_	in	A(c)]for	_	in	A(c)]
	for	k	in	A(c):
		for	B	in	A(c):
			if	j[k][B]==5:
				for	l	in	A(max(0,k-1),min(c,k+2)):
					for	D	in	A(max(0,B-1),min(c,B+2)):C[l][D]=1
	return	C