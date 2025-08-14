A=range
def	p(g):h=len(g);n=h*2;return[[sum(g[r-k][c-k]if	0<=r-k<h	and	0<=c-k<h	else	0for	k	in	A(n))for	c	in	A(n)]for	r	in	A(n)]