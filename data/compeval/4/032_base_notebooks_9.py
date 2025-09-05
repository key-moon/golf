def	p(m):
	t=len(m);s=[[0]*len(m[0])for	_	in	m]
	for	j	in	range(len(m[0])):
		c=[m[i][j]for	i	in	range(t)if	m[i][j]]
		for(i,x)in	enumerate(c):s[t-len(c)+i][j]=x
	return	s