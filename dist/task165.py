A=range
def	p(g):
	c=[next(filter(int,s))for	s	in	g	if	any(s)][-1]
	for	B	in	A(400):
		for	k	in	A(i:=B%20,0,-1):
			if	c==g[i][j:=B//20]!=g[k][j]>0:
				for	s	in	g[k+1:20]:s[j]=g[i][j]
				break
	return	g