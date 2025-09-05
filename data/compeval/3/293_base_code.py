def	p(g):
	A={}
	for(i,D)in	enumerate(g):
		for(j,v)in	enumerate(D):
			if	v:a=A.setdefault(v,(set(),set()));a[0].add(i);a[1].add(j)
	h=w=0
	for(k,(B,C))in	A.items():
		if	len(B)<len(C):h=k
		else:w=k
	B,C=A[h][0],A[w][1];i,j=next(iter(B)),next(iter(C));d=h	if	g[i][j]==w	else	w
	for	i	in	B:
		for	j	in	C:g[i][j]=d
	return	g