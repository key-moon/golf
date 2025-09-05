def	p(input):
	n=len(input);o=[[0]*(2*n)for	_	in	range(2*n)]
	for	i	in	range(n):
		for	j	in	range(n):o[i][j]=input[i][j];o[i][2*n-j-1]=input[i][j];o[2*n-i-1][j]=input[i][j];o[2*n-i-1][2*n-j-1]=input[i][j]
	return	o