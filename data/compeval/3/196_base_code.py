def	p(g):
	v=set();n=len(g);m=len(g[0])
	for	i	in	range(n):
		for	j	in	range(m):
			if	g[i][j]and(i,j)not	in	v:
				c=[(i,j)];f=[(i,j)];v.add((i,j))
				while	f:
					x,y=f.pop()
					for(C,D)in(1,0),(0,1),(-1,0),(0,-1):
						u,b=x+C,y+D
						if	0<=u<n	and	0<=b<m	and	g[u][b]and(u,b)not	in	v:v.add((u,b));f+=[(u,b)];c+=[(u,b)]
				a,b=zip(*c);A,B=max(a)-min(a)+1,max(b)-min(b)+1
				if	A>1and	B>1and	len(c)==2*(A+B)-4:
					for(x,y)in	c:g[x][y]=3
	return	g