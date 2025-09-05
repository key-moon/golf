def	p(m,u=range):
	r,c,n=len(m),len(m[0]),0;v=[[0]*c	for	_	in	m]
	def	d(y,x):
		s=[(y,x)];v[y][x]=1
		while	s:
			y,x=s.pop()
			for(B,C)in[(-1,0),(1,0),(0,-1),(0,1)]:
				b,A=y+B,x+C
				if	0<=b<r	and	0<=A<c	and	m[b][A]and	not	v[b][A]:v[b][A]=1;s+=[(b,A)]
	for	y	in	u(r):
		for	x	in	u(c):
			if	m[y][x]and	not	v[y][x]:n+=1;d(y,x)
	return[[8*(i==j)for	j	in	u(n)]for	i	in	u(n)]