def	p(g):
	h,w=len(g),len(g[0]);v=[[0]*w	for	_	in	range(h)];q=[]
	for	i	in	range(h):
		for	j	in	range(w):
			if	i*j==0	or	i==h-1or	j==w-1:
				if	g[i][j]==0:v[i][j]=1;q.append((i,j))
	while	q:
		r,c=q.pop(0)
		for(C,D)in[(-1,0),(1,0),(0,-1),(0,1)]:
			A,B=r+C,c+D
			if	0<=A<h	and	0<=B<w	and	g[A][B]==0and	not	v[A][B]:v[A][B]=1;q.append((A,B))
	E=[[g[i][j]if	g[i][j]!=0	or	v[i][j]else	1for	j	in	range(w)]for	i	in	range(h)];return	E