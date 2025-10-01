def	p(g):
	for	i	in	range(n:=len(g)):
		for	l	in	range(n):
			if(s:=g[i])[r:=l]>8:
				while	s[r:]>[8]:r+=1
				for	t	in	g[i:]:
					for	j	in	range(l,r):t[j]|=1
				for	k	in	range(i-(u:=r-l>>1),i+u+1):
					for	j	in	range(l-u,r+u):
						if-1<k<n>j>-1and	g[k][j]<9:g[k][j]=3
	return	g