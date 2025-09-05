def	p(g,E=enumerate):
	o=[[0]*len(g[0])for	_	in	g]
	for	v	in	set(sum(g,[]))-{0}:
		A=[(i,j)for(i,r)in	E(g)for(j,x)in	E(r)if	x==v];b,m=max(i	for(i,_)in	A),max(j	for(_,j)in	A)
		for(i,j)in	A:o[i][j+(i<b	and	j<m)]=v
	return	o