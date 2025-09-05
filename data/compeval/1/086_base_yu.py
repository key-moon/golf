def	p(g):
	c,d,_=sorted({*sum(g,[])},key=sum(g,[]).count);u=[s[:]for	s	in	g]
	for	i	in	range(len(g)):
		for	j	in	range(len(g[0])):
			for	k	in	range(4):
				if	any(all(len(g)>i+~-abs(k-1)*t>-1<j+~-abs(k-2)*t<len(g[0])and	d==g[i+~-abs(k-1)*t][j+~-abs(k-2)*t]for	t	in[s//2+1,s+3])for	s	in	range(3)):u[i][j]=d
			if	g[i][j]:u[i][j]=g[i][j]^c^d
	return	u