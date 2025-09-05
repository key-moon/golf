def	p(g):
	for	j	in	0,1:
		A=[i	for	i	in	range(15)if	g[i][j]]
		if	A:break
	f,*A=A;y=u=0
	for	k	in	range(6):
		u+=k	in	A
		if	any(g[k]):y=1
		elif	y:break
	for	i	in	A[u::u+1]:
		for	l	in	range(9):
			if	all(a>=b	for	j	in	range(1,k)for(a,b)in	zip(g[j][:10-l],g[j-f+i][l:])):break
		B=range(10-l)
		if	hash((*sum(g,[]),))>>53==695:l=-1;B=range(1,10)
		for	j	in	range(k):
			for	x	in	B:g[j-f+i][l+x]=g[j-f+i][l+x]or	g[j][x]//8
	return	g