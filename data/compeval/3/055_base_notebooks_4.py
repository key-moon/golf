def	p(g):
	q=range;r=[o[:]for	o	in	g];m,n=len(g),len(g[0]);v=next(g[i][j]for	i	in	q(m)for	j	in	q(n)if	g[i][j]);c=[j	for	j	in	q(n)if	all(g[i][j]==v	for	i	in	q(m))];h=[i	for	i	in	q(m)if	all(g[i][j]==v	for	j	in	q(n))]
	for	i	in	q(m):
		for	j	in	q(n):
			if	h[0]<i<h[1]and	c[0]<j<c[1]:r[i][j]=6
			elif	i<h[0]and	c[0]<j<c[1]:r[i][j]=2
			elif	i>h[1]and	c[0]<j<c[1]:r[i][j]=1
			elif	j<c[0]and	h[0]<i<h[1]:r[i][j]=4
			elif	j>c[1]and	h[0]<i<h[1]:r[i][j]=3
	return	r