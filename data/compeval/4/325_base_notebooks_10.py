def	p(m,K=range):
	r,c=len(m),len(m[0]);n=0
	def	f(y,x):
		m[y][x]=0
		for(b,a)in(1,0),(-1,0),(0,1),(0,-1):
			A,B=y+b,x+a
			if	0<=A<r	and	0<=B<c	and	m[A][B]:f(A,B)
	for	i	in	K(r):
		for	j	in	K(c):
			if	m[i][j]:n+=1;f(i,j)
	return[[8*(i==j)for	j	in	K(n)]for	i	in	K(n)]