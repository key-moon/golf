def	p(j):
	A=range;c=[[0]*3for	_	in	A(3)]
	for	C	in	A(3):
		for	k	in	A(3):
			B={}
			for	l	in	A(3):
				for	D	in	A(3):a=j[C*3+l][k*3+D];B[a]=B.get(a,0)+1
			c[C][k]=max(B,key=B.get)
	return	c