def	p(R,u=range):
	n=len(R);o=[[0]*(2*n)for	_	in	u(2*n)]
	for	i	in	u(n):
		for	j	in	u(n):o[i][j]=R[i][j];o[i][2*n-j-1]=R[i][j];o[2*n-i-1][j]=R[i][j];o[2*n-i-1][2*n-j-1]=R[i][j]
	return	o