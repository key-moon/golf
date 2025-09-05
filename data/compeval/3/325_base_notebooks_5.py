def	p(m,k=range):
	r,c,n=len(m),len(m[0]),0;v=[[0]*c	for	_	in	m]
	def	d(y,x):
		s=[(y,x)];v[y][x]=1
		while	s:
			y,x=s.pop()
			for(g,C)in[(-1,0),(1,0),(0,-1),(0,1)]:
				A,B=y+g,x+C
				if	0<=A<r	and	0<=B<c	and	m[A][B]and	not	v[A][B]:v[A][B]=1;s+=[(A,B)]
	for	y	in	k(r):
		for	x	in	k(c):
			if	m[y][x]and	not	v[y][x]:n+=1;d(y,x)
	return[[8*(i==j)for	j	in	k(n)]for	i	in	k(n)]