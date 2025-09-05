def	p(g):
	A=[i	for(i,r)in	enumerate(g)for	v	in	r	if	v==2];B=[j	for	r	in	g	for(j,v)in	enumerate(r)if	v==2];a,b=min(A),max(A);c,d=min(B),max(B);n=[[0]*len(g[0])for	_	in	g]
	for(i,r)in	enumerate(g):
		for(j,v)in	enumerate(r):
			if	v==2:n[i][j]=2
			if	v==5:C=a-1if	i<a	else	b+1if	i>b	else	i;D=c-1if	j<c	else	d+1if	j>d	else	j;n[C][D]=5
	return	n