def	p(g,E=enumerate):
	a,b=zip(*((i,j)for(i,r)in	E(g)for(j,v)in	E(r)if	v))
	for(u,v)in(0,0),(-1,0),(1,0),(0,-1),(0,1):g[sum(a)//2+u][sum(b)//2+v]=3
	return	g