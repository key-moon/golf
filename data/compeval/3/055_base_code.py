def	p(g):
	m,n=len(g),len(g[0]);a,b=[i	for(i,r)in	enumerate(g)if	r==[8]*n];x,y=[j	for	j	in	range(n)if[r[j]for	r	in	g]==[8]*m]
	for	i	in	range(m):
		for	j	in	range(n):
			if	g[i][j]==0:
				if	a<i<b:g[i][j]=6if	x<j<y	else	4if	j<x	else	3
				elif	x<j<y:g[i][j]=2if	i<a	else	1
	return	g