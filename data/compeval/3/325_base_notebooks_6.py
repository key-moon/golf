def	p(j,A=range):
	c,B=len(j),len(j[0]);k=0
	def	f(W,l):
		j[W][l]=0
		for(C,a)in(1,0),(-1,0),(0,1),(0,-1):
			A,e=W+C,l+a
			if	0<=A<c	and	0<=e<B	and	j[A][e]:f(A,e)
	for	C	in	A(c):
		for	w	in	A(B):
			if	j[C][w]:k+=1;f(C,w)
	return[[8*(B==w)for	w	in	A(k)]for	B	in	A(k)]