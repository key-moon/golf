def	p(g):
	m,n=len(g),len(g[0]);v=[[0]*n	for	_	in	g]
	for	i	in	range(m):
		for	j	in	range(n):
			if	g[i][j]==2and	not	v[i][j]:
				C=[(i,j)];D=[];v[i][j]=1
				while	C:
					x,y=C.pop();D.append((x,y))
					for(G,H)in(1,0),(-1,0),(0,1),(0,-1):
						A,B=x+G,y+H
						if	0<=A<m	and	0<=B<n	and	g[A][B]==2and	not	v[A][B]:v[A][B]=1;C.append((A,B))
				E=[x	for(x,y)in	D];a,b=min(E),max(E);d=(b-a+1)//2;F=b-d+1
				for	r	in	range(F,b+1):
					t=r-F+1;I=sorted(y	for(x,y)in	D	if	x==r)
					for	y	in	I[:t]:g[r][y]=8
	return	g