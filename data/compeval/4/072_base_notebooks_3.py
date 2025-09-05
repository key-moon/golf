def	p(g):
	for(i,r)in	enumerate(g):
		if	all(c==4for	c	in	r):t,b=g[:i],g[i+1:i+1+i];return[[3if(t[r][c]!=0)!=(b[r][c]!=0)else	0for	c	in	range(len(t[0]))]for	r	in	range(len(t))]