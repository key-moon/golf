def	p(m,F=range):
	r,c,n=len(m),len(m[0]),0;v=[[0]*c	for	_	in	m]
	def	d(y,x):
		s=[(y,x)];v[y][x]=1
		while	s:
			y,x=s.pop()
			for(B,C)in[(-1,0),(1,0),(0,-1),(0,1)]:
				A,a=y+B,x+C
				if	0<=A<r	and	0<=a<c	and	m[A][a]and	not	v[A][a]:v[A][a]=1;s+=[(A,a)]
	for	y	in	F(r):
		for	x	in	F(c):
			if	m[y][x]and	not	v[y][x]:n+=1;d(y,x)
	return[[8*(i==j)for	j	in	F(n)]for	i	in	F(n)]