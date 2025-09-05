def	p(g):
	for	y	in	range(5):
		for	x	in	range(5):
			if	g[y][x]and	g[y][x+1]and	g[y+1][x]and	g[y+1][x+1]:C,D=y,x;break
		else:continue
		break
	a=g[C][D];b=g[C][D+1];c=g[C+1][D];d=g[C+1][D+1]
	for(i,j)in(0,0),(0,1),(1,0),(1,1):
		A,B=C-1-i,D-1-j
		if	0<=A<6and	0<=B<6and	g[A][B]==0:g[A][B]=d
	for(i,j)in(0,0),(0,1),(1,0),(1,1):
		A,B=C-1-i,D+2+j
		if	0<=A<6and	0<=B<6and	g[A][B]==0:g[A][B]=c
	for(i,j)in(0,0),(0,1),(1,0),(1,1):
		A,B=C+2+i,D-1-j
		if	0<=A<6and	0<=B<6and	g[A][B]==0:g[A][B]=b
	for(i,j)in(0,0),(0,1),(1,0),(1,1):
		A,B=C+2+i,D+2+j
		if	0<=A<6and	0<=B<6and	g[A][B]==0:g[A][B]=a
	return	g