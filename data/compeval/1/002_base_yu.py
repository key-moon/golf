def	p(g):
	for	d	in	range(len(g)):
		for	r	in	range(len(g[0])):
			for	l	in	range(1,r):
				for	u	in	range(1,d):
					v=g[u:d]
					if	sum(sum(s[l:r])for	s	in	v)<all(g[d][l:r]+g[u-1][l:r]+[s[l-1]&s[r]for	s	in	v]):
						for	s	in	v:s[l:r]=[4]*(r-l)
	return	g