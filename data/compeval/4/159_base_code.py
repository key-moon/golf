def	p(g):
	t=[(i,j)for(i,r)in	enumerate(g)for(j,v)in	enumerate(r)if	v==2];a=min(i	for(i,j)in	t);b=min(j	for(i,j)in	t);h=max(i	for(i,j)in	t)-a+1;B=[[0]*h	for	_	in	range(h)]
	for(i,j)in	t:B[i-a][j-b]=2
	k=next(v	for	r	in	g	for	v	in	r	if	v*(v-2));A=[(i,j)for(i,r)in	enumerate(g)for(j,v)in	enumerate(r)if	v==k];c=min(i	for(i,j)in	A);d=min(j	for(i,j)in	A);s=(h-2)//(max(i	for(i,j)in	A)-c+1)
	for(i,j)in	A:
		for	x	in	range(s):
			for	y	in	range(s):B[1+(i-c)*s+x][1+(j-d)*s+y]=k
	return	B