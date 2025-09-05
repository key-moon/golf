def	p(g,F=range):
	h,w=len(g),len(g[0]);s=[0for	_	in	F(w)]
	for	i	in	F(w):
		for	j	in	F(h):
			if	g[j][i]>0:s[i]+=1
			g[j][i]=0
	m=min([c	for	c	in	s	if	c>0]);i=s.index(m)
	for	j	in	F(s[i]):g[-(j+1)][i]=2
	i=s.index(max(s))
	for	j	in	F(s[i]):g[-(j+1)][i]=1
	return	g