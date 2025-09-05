def	p(g):
	n,m=len(g),len(g[0]);v=[[0]*m	for	_	in	g];f={}
	for	i	in	range(n):
		for	j	in	range(m):
			if	g[i][j]and	not	v[i][j]:
				s=[(i,j)];v[i][j]=1;c=[]
				while	s:
					x,y=s.pop();c.append((x,y))
					for(E,F)in(1,0),(-1,0),(0,1),(0,-1):
						C,D=x+E,y+F
						if	0<=C<n	and	0<=D<m	and	g[C][D]and	not	v[C][D]:v[C][D]=1;s.append((C,D))
				A=min(x	for(x,_)in	c);B=min(y	for(_,y)in	c);k=tuple(sorted((a-A,b-B)for(a,b)in	c));f.setdefault(k,[]).append((A,B,c))
	for(k,l)in	f.items():
		for(A,B,c)in	l:
			if	len({g[a][b]for(a,b)in	c})>1:z=A,B,c;break
		G={(a-z[0],b-z[1]):g[a][b]for(a,b)in	z[2]}
		for(A,B,c)in	l:
			if	c!=z[2]:
				for(a,b)in	c:g[a][b]=G[a-A,b-B]
	return	g