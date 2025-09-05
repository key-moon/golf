def	p(g):
	d={}
	for(i,r)in	enumerate(g):
		for(j,v)in	enumerate(r):
			if	v:d.setdefault(v,[]).append((i,j))
	for(v,p)in	d.items():
		(A,B),(C,D)=p
		for	i	in	range(min(A,C),max(A,C)+1):
			for	j	in	range(min(B,D),max(B,D)+1):
				if	g[i][j]==0and(i==A	or	i==C	or	j==B	or	j==D):g[i][j]=v
	return	g