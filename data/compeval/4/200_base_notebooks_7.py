def	p(g):
	n,B,A,t=10,enumerate,range,0
	for(i,a)in	B(g):
		for(j,v)in	B(a):
			if	v%5:
				for	c	in	A(j,n,2):
					for	r	in	A(i+1):g[r][c]=v
				for	c	in	A(j+1,n,2):g[t*(n-1)][c]=5;t^=1
				return	g