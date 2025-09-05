def	p(g):
	C,D=len(g),len(g[0]);A={(i,j)for	i	in	range(C)for	j	in	range(D)if	g[i][j]==2}
	while	A:
		i,j=A.pop();a=b=i;c=d=j;B=[(i,j)]
		while	B:
			x,y=B.pop()
			for(u,v)in(x+1,y),(x-1,y),(x,y+1),(x,y-1):
				if(u,v)in	A:
					A.remove((u,v));B.append((u,v))
					if	u<a:a=u
					elif	u>b:b=u
					if	v<c:c=v
					elif	v>d:d=v
		if	b>a	or	d>c:
			for	x	in	range(a-1,b+2):
				if	0<=x<C:
					for	y	in	range(c-1,d+2):
						if	0<=y<D	and	g[x][y]==0and(x<a	or	x>b	or	y<c	or	y>d):g[x][y]=3
	return	g