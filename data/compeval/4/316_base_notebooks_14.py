def	p(j):
	A=3;c=[]
	for	B	in	zip(*j):
		for	k	in	B:
			if	k:c+=[k];break
	c+=[0]*(A*A-len(c));return[c[k*A:k*A+A][::1-2*(k%2)]for	k	in	range(A)]