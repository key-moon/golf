def	p(m):
	a,b=len(m),len(m[0]);v=[[0]*b	for	_	in	m];r=[]
	def	f(i,j):
		q=[(i,j)];v[i][j]=1;c=[(i,j)];d=1
		while	q:
			x,y=q.pop()
			for(u,C)in[(0,1),(1,0),(0,-1),(-1,0)]:
				A,B=x+u,y+C
				if	not(0<=A<a	and	0<=B<b):d=0;continue
				if	m[A][B]<1and	not	v[A][B]:v[A][B]=1;q+=[(A,B)];c+=[(A,B)]
		return	c	if	d	else[]
	for	i	in	range(a):
		for	j	in	range(b-1,-1,-1):
			if	m[i][j]<1and	not	v[i][j]:r+=[f(i,j)]
	r.sort(key=len,reverse=1)
	for(i,x)in	enumerate(r):
		t=min(8,max(6,len(x)**.5+.0+5))
		for	y	in	x:m[y[0]][y[1]]=t
	return	m