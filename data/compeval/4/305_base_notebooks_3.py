def	p(m):
	n=len(m);f=[x	for	r	in	m	for	x	in	r	if	x]
	if	not	f:return	m
	b=sorted(set(f));s=len(b);o=[[0]*n	for	_	in[0]*n]
	for	i	in	range(n):
		for	j	in	range(n):o[i][j]=b[(i+j)%s]
	return	o