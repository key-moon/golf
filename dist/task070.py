B=range
A=enumerate
def	p(g):
	C,D=zip(*[(i,j)for(i,r)in	A(g)for(j,v)in	A(r)if	v==8]);a,b=min(C),max(C);c,d=min(D),max(D)
	for	i	in	B(a,b+1):
		for	j	in	B(c,d+1):
			if	g[i][j]^8:g[i][j]=3
	return	g