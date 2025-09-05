def	p(g):
	h,w=len(g),len(g[0]);u=sorted((x,i,j,r,d)for	A	in	range(h*w)if(i:=A%h)<1or	g[i-1][j]if(j:=A//h)<1or	g[i][j-1]if(x:=(r:=[*g[i][j:],2].index(2))*(d:=[*(g[k][j]for	k	in	range(i,h)),2].index(2))))
	for(x,i,j,d,r)in	u:
		for	s	in	g[i:i+r]:
			if	x==u[0][0]:s[j:j+d]=[8]*d
			if	x==u[-1][0]:s[j:j+d]=[1]*d
	return	g