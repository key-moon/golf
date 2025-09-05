def	α(a,c):return	len(set([r[c]for	r	in	a]))
def	p(g):
	A=enumerate;h,w=len(g),len(g[0]);B=α(g,0)+α(g,-1)<len(set(g[0]))+len(set(g[-1]));g=[[A	if	A!=5else	0for	A	in	A]for	A	in	g]
	for(r,C)in	A(g):
		for(c,D)in	A(C):
			if	B:g[r][c]=max([g[0][c],g[-1][c]])
			else:g[r][c]=max([g[r][0],g[r][-1]])
	if	B:g=[[c	for	c	in	A	if	c>0]for	A	in	g];g=g[:len(g[0])]
	else:g=[A	for	A	in	g	if	sum(A)>0];g=[A[:len(g)]for	A	in	g]
	return	g