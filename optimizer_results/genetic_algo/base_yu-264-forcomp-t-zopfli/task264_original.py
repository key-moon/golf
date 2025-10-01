def	p(g):
	o=[[5]*9for	_	in	range(9)]
	for	i	in	range(len(g)-2):
		for	j	in	range(len(g[i])-2):
			for	u	in	range(3*(g[i][j]>0)):o[(1+(g[i+2][j+1]!=5)-(g[i][j+1]!=5))*3+u][(1+(g[i+1][j+2]!=5)-(g[i+1][j]!=5))*3:(1+(g[i+1][j+2]!=5)-(g[i+1][j]!=5))*3+3]=g[i+u][j:j+3]
			for	u	in	range(3*(g[i][j]>0)):g[i+u][j:j+3]=[0]*3
	return	o