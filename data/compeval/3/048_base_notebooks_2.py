def	p(g):
	t=range;d=abs;m,n=len(g),len(g[0]);s=[(i,j)for	i	in	t(m-1)for	j	in	t(n-1)if	all(g[i+x][j+y]==2for	x	in[0,1]for	y	in[0,1])];q=[(i,j)for	i	in	t(m)for	j	in	t(n)if	g[i][j]==8and	any(d(i-s[0][0]-x)+d(j-s[0][1]-y)==1for	x	in[0,1]for	y	in[0,1])];v=set(q)
	while	q:
		i,j=q.pop(0)
		for(x,y)in[(0,1),(1,0),(0,-1),(-1,0)]:
			c,w=i+x,j+y
			if	0<=c<m	and	0<=w<n	and	g[c][w]==8and(c,w)not	in	v:v.add((c,w));q.append((c,w))
			if	any(d(c-s[1][0]-a)+d(w-s[1][1]-b)==0for	a	in[0,1]for	b	in[0,1]):return[[8]]
	return[[0]]