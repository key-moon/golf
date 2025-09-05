def	p(g):
	for	d	in	range(len(g)+1):
		for	r	in	range(len(g[0])+1):
			for	u	in	range(d):
				for	l	in	range(r):
					if(u>0and	0in	g[u-1][l:r])+(d<len(g)and	0in	g[d][l:r])+(l>0and	0in[g[i][l-1]for	i	in	range(u,d)])+(r<len(g[0])and	0in[g[i][r]for	i	in	range(u,d)])+sum(sum(s[l:r])for	s	in	g[u:d])+any(len(g[0])>j>-1<i<len(g)and	g[i][j]>4for(i,j)in[[u-2,l-1],[u-2,r],[d+1,l-1],[d+1,r],[u-1,l-2],[u-1,r+1],[d,l-2],[d,r+1]])<1:
						for	s	in	g[u:d]:s[l:r]=[4]*(r-l)
	return	g