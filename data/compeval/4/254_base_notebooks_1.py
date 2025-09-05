def	p(g,v=range):
	h,w=len(g),len(g[0]);s=[0for	_	in	v(w)]
	for	i	in	v(w):
		for	j	in	v(h):
			if	g[j][i]>0:s[i]+=1
			g[j][i]=0
	m=min([c	for	c	in	s	if	c>0]);i=s.index(m)
	for	j	in	v(s[i]):g[-(j+1)][i]=2
	i=s.index(max(s))
	for	j	in	v(s[i]):g[-(j+1)][i]=1
	return	g