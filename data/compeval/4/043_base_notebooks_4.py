def	p(g):
	A=enumerate;h=len(g)-1;w=len(g[0])-1
	for(r,B)in	A(g):
		for(c,C)in	A(B):
			if	r>0and	c<h:
				if	g[r][w]==5and	g[0][c]==5:g[r][c]=2
	return	g