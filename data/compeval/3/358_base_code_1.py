def	p(g):
	n=len(g);m=len(g[0]);r=max(range(n),key=lambda	i:sum(map(bool,g[i])));a=[x	for	x	in	g[r]if	x];k=g[r].index(a[0]);c=max(range(m),key=lambda	j:sum(g[i][j]!=0for	i	in	range(n)));b=[g[i][c]for	i	in	range(n)if	g[i][c]];l=next(i	for	i	in	range(n)if	g[i][c]);g[r]=[a[(j-k)%len(a)]for	j	in	range(m)]
	for	i	in	range(n):g[i][c]=b[(i-l)%len(b)]
	return	g