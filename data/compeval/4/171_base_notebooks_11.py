def	p(T,u=range):
	A=len(T);B=len(T[0]);s=[[0for	_	in	u(B)]for	_	in	u(A)]
	for	r	in	u(A):
		for	c	in	u(B):
			if	r==0	or	r==A-1or	c==0	or	c==B-1:s[r][c]=8
			else:s[r][c]=0
	return	s