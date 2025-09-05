def	p(g):
	c=max(sum(g,[]),key=sum(g,[]).count);_,l,r,u,d=max((sum((v==c)-.6for	s	in	g[u:d]for	v	in	s[l:r]),l,r,u,d)for	d	in	range(len(g))for	r	in	range(len(g[0]))for	l	in	range(r)for	u	in	range(d));s=[s[l:r]for	s	in	g[u:d]];u=sum([[i,j]for	i	in	range(len(s))for	j	in	range(len(s[i]))if	s[i][j]!=c],[])
	for	i	in	range(len(s)):
		for	j	in	range(len(s[i])):
			if	i	in	u[::2]or	j	in	u[1::2]:s[i][j]=s[u[0]][u[1]]
	return	s