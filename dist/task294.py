A=range
p=lambda	g:[[2if	g[i][j]==5and	all(0<=i+d[0]<10and	0<=j+d[1]<10and	g[i+d[0]][j+d[1]]==5for	d	in[(-1,0),(1,0),(0,-1),(0,1)])else	g[i][j]for	j	in	A(10)]for	i	in	A(10)]