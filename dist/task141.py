B=range
A=enumerate
def	p(g):n=len(g);a,b=next((i,j)for(i,B)in	A(g)for(j,x)in	A(B)if	x);v=g[a][b];return[[v	if	abs(r-a)==abs(c-b)else	0for	c	in	B(n)]for	r	in	B(n)]