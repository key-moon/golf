def	p(m,u=range):
	r,c,n=len(m),len(m[0]),0;v=[[0]*c	for	_	in	m]
	def	d(y,x):
		s=[(y,x)];v[y][x]=1
		while	s:
			y,x=s.pop()
			for(B,C)in[(-1,0),(1,0),(0,-1),(0,1)]:
				A,e=y+B,x+C
				if	0<=A<r	and	0<=e<c	and	m[A][e]and	not	v[A][e]:v[A][e]=1;s+=[(A,e)]
	for	y	in	u(r):
		for	x	in	u(c):
			if	m[y][x]and	not	v[y][x]:n+=1;d(y,x)
	return[[8*(i==j)for	j	in	u(n)]for	i	in	u(n)]