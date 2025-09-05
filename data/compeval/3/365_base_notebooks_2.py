def	p(g):
	A=range;b,v=[],set()
	for	i	in	A(10):
		for	j	in	A(10):
			if	g[i][j]and(i,j)not	in	v:
				r=j
				while	r<10and	g[i][r]:r+=1
				r-=1;t=i
				while	t<10and	all(g[t][k]for	k	in	A(j,r+1)):t+=1
				t-=1;k=[[g[u][w]for	w	in	A(j,r+1)]for	u	in	A(i,t+1)]
				for	u	in	A(i,t+1):
					for	w	in	A(j,r+1):v.add((u,w))
				b.append((sum(sum(x==2for	x	in	A)for	A	in	k),k))
	return	max(b)[1]