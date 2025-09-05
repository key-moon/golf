def	p(g):
	d={}
	for(i,r)in	enumerate(g):
		for(j,v)in	enumerate(r):
			if	v:d.setdefault(v,[]).append((i,j))
	for(v,l)in	d.items():
		i,j=l[0];x,y=l[1];A=(x>i)-(x<i);B=(y>j)-(y<j)
		while	1:
			g[i][j]=v
			if	i==x	and	j==y:break
			i+=A;j+=B
	return	g