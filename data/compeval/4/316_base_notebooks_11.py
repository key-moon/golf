def	p(j):
	A=3;c=[]
	for	B	in	zip(*j):
		for	k	in	B:
			if	k:c+=[k];break
	c+=[0]*(A*A-len(c));return[c[i*A:i*A+A][::1-2*(i%2)]for	i	in	range(A)]