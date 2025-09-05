def	p(g):
	n,m=len(g),len(g[0]);v=[[0]*m	for	_	in	g];s=[(i,j)for	i	in(0,n-1)for	j	in	range(m)if	g[i][j]==0]+[(i,j)for	j	in(0,m-1)for	i	in	range(n)if	g[i][j]==0]
	for(i,j)in	s:v[i][j]=1
	while	s:
		i,j=s.pop()
		if	i>0and	not	v[i-1][j]and	g[i-1][j]==0:v[i-1][j]=1;s.append((i-1,j))
		if	i+1<n	and	not	v[i+1][j]and	g[i+1][j]==0:v[i+1][j]=1;s.append((i+1,j))
		if	j>0and	not	v[i][j-1]and	g[i][j-1]==0:v[i][j-1]=1;s.append((i,j-1))
		if	j+1<m	and	not	v[i][j+1]and	g[i][j+1]==0:v[i][j+1]=1;s.append((i,j+1))
	for	i	in	range(n):
		for	j	in	range(m):
			if	g[i][j]==0and	not	v[i][j]:g[i][j]=4
	return	g