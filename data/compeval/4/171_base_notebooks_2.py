def	p(X,j=range):
	v=len(X);b=len(X[0]);u=[[0for	_	in	j(b)]for	_	in	j(v)]
	for	r	in	j(v):
		for	c	in	j(b):
			if	r==0	or	r==v-1or	c==0	or	c==b-1:u[r][c]=8
			else:u[r][c]=0
	return	u