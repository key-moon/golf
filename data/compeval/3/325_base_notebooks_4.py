def	p(m,D=range):
	r,c,n=len(m),len(m[0]),0;v=[[0]*c	for	_	in	m]
	def	d(y,x):
		s=[(y,x)];v[y][x]=1
		while	s:
			y,x=s.pop()
			for(b,g)in[(-1,0),(1,0),(0,-1),(0,1)]:
				A,B=y+b,x+g
				if	0<=A<r	and	0<=B<c	and	m[A][B]and	not	v[A][B]:v[A][B]=1;s+=[(A,B)]
	for	y	in	D(r):
		for	x	in	D(c):
			if	m[y][x]and	not	v[y][x]:n+=1;d(y,x)
	return[[8*(i==j)for	j	in	D(n)]for	i	in	D(n)]