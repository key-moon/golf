def	p(g):
	m,n=len(g),len(g[0]);v=[[0]*n	for	_	in	g];d=(1,0),(-1,0),(0,1),(0,-1);b=[(i,j)for	i	in	range(m)for	j	in(0,n-1)]+[(i,j)for	j	in	range(n)for	i	in(0,m-1)]
	for(i,j)in	b:
		if	g[i][j]==0and	not	v[i][j]:
			A=[(i,j)];v[i][j]=1
			while	A:
				a,B=A.pop()
				for(u,w)in	d:
					x,y=a+u,B+w
					if	0<=x<m	and	0<=y<n	and	g[x][y]==0and	not	v[x][y]:v[x][y]=1;A.append((x,y))
	for	i	in	range(m):
		for	j	in	range(n):
			if	g[i][j]==0and	not	v[i][j]:
				A=[(i,j)];v[i][j]=1;E=[(i,j)];F=i;G=i;C=j;D=j
				while	A:
					a,B=A.pop()
					for(u,w)in	d:
						x,y=a+u,B+w
						if	0<=x<m	and	0<=y<n	and	g[x][y]==0and	not	v[x][y]:v[x][y]=1;A.append((x,y));E.append((x,y));F=min(F,x);G=max(G,x);C=min(C,y);D=max(D,y)
				c=7if(D-C+1)%2else	2
				for(a,B)in	E:g[a][B]=c
	return	g