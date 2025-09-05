def	p(g):
	h,w=len(g),len(g[0]);s=[(i,j,g[i][j])for	i	in	range(h)for	j	in	range(w)if	g[i][j]];o=[[0]*w	for	_	in	range(h)]
	for	i	in	range(h):
		for	j	in	range(w):
			d=[abs(i-x)+abs(j-y)for(x,y,_)in	s];m=min(d)
			if	d.count(m)==1:
				x,y,v=s[d.index(m)]
				if	max(abs(i-x),abs(j-y))%2<1:o[i][j]=v
	return	o