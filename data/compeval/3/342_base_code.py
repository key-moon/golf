def	p(g):
	r,c=sorted((i,j)for	i	in	range(10)for	j	in	range(10)if	g[i][j]==8)[0];s=sorted((i,j,x)for	i	in	range(10)for	j	in	range(10)if(x:=g[i][j])%8);a=sorted(s[:2],key=lambda	x:x[1]);b=sorted(s[2:],key=lambda	x:x[1])
	for	i	in	range(10):g[i]=[0]*10
	g[r][c],g[r][c+1]=a[0][2],a[1][2];g[r+1][c],g[r+1][c+1]=b[0][2],b[1][2];return	g