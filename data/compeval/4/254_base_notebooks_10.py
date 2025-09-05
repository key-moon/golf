def	p(g,u=range):
	h,w=len(g),len(g[0]);s=[0for	_	in	u(w)]
	for	i	in	u(w):
		for	j	in	u(h):
			if	g[j][i]>0:s[i]+=1
			g[j][i]=0
	m=min([c	for	c	in	s	if	c>0]);i=s.index(m)
	for	j	in	u(s[i]):g[-(j+1)][i]=2
	i=s.index(max(s))
	for	j	in	u(s[i]):g[-(j+1)][i]=1
	return	g