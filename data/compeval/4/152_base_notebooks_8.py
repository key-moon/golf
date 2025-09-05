def	p(D,v=range):
	n=len(D);o=[[0]*(2*n)for	_	in	v(2*n)]
	for	i	in	v(n):
		for	j	in	v(n):o[i][j]=D[i][j];o[i][2*n-j-1]=D[i][j];o[2*n-i-1][j]=D[i][j];o[2*n-i-1][2*n-j-1]=D[i][j]
	return	o