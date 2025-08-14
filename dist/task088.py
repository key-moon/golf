B=range
A=enumerate
def	p(g):s=sum(g,[]);u=[x	for	x	in	set(s)if	s.count(x)==4][0];w=[(i,j)for(i,r)in	A(g)for(j,x)in	A(r)if	x==u];a,b=w[0];c,d=w[-1];return[[u	if	g[i][j]else	0for	j	in	B(b+1,d)]for	i	in	B(a+1,c)]