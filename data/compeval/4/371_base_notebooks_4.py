def	p(j,A=enumerate):
	c,B=zip(*((i,j)for(i,r)in	A(j)for(j,B)in	A(r)if	B))
	for(k,C)in(0,0),(-1,0),(1,0),(0,-1),(0,1):j[sum(c)//2+k][sum(B)//2+C]=3
	return	j