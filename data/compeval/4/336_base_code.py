def	p(g):
	r,c=len(g),len(g[0]);C=min(i	for	i	in	range(r)for	j	in	range(c)if	g[i][j]==5);D=max(i	for	i	in	range(r)for	j	in	range(c)if	g[i][j]==5);E=min(j	for	i	in	range(r)for	j	in	range(c)if	g[i][j]==5);F=max(j	for	i	in	range(r)for	j	in	range(c)if	g[i][j]==5)
	for	k	in	range(E,F+1):
		if	g[C][k]==0:A,B=C,k;break
	else:
		for	k	in	range(E,F+1):
			if	g[D][k]==0:A,B=D,k;break
		else:
			for	i	in	range(C,D+1):
				if	g[i][E]==0:A,B=i,E;break
			else:
				for	i	in	range(C,D+1):
					if	g[i][F]==0:A,B=i,F;break
	for	i	in	range(C+1,D):
		for	j	in	range(E+1,F):
			if	g[i][j]==0:g[i][j]=8
	if	A==C:
		for	i	in	range(A+1):g[i][B]=8
	elif	A==D:
		for	i	in	range(A,r):g[i][B]=8
	elif	B==E:
		for	k	in	range(B+1):g[A][k]=8
	else:
		for	k	in	range(B,c):g[A][k]=8
	return	g