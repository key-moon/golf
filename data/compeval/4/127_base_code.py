def	p(g):
	n,m=len(g),len(g[0]);h=[i	for	i	in	range(n)if	g[i]==[5]*m];y=h	and[0]+h+[n]or[0,n];w=[j	for	j	in	range(m)if	all(g[i][j]==5for	i	in	range(n))];x=[0]+w+[m]
	for	p	in	range(len(y)-1):
		for	q	in	range(len(x)-1):
			A=y[p]+(p>0);C=y[p+1];B=x[q]+(q>0);D=x[q+1];v=g[A+(C-A)//2][B+(D-B)//2]+5
			for	i	in	range(A,C):
				for	j	in	range(B,D):g[i][j]=v
	return	g