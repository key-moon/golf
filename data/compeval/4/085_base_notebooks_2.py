def	p(g):
	r=[A[:]for	A	in	g];v=set()
	for	i	in	range(len(g)-2):
		for	j	in	range(len(g[0])):
			if	g[i][j]and(i,j)not	in	v:
				c=g[i][j]
				if	all(g[i+k][j]==c	for	k	in	range(3)):
					A=j
					while	A<len(g[0])and	all(g[i+k][A]==c	for	k	in	range(3)):
						for	k	in	range(3):v.add((i+k,A))
						A+=1
					for	x	in	range(j,A):
						if(x-j)%2==1:r[i+1][x]=0
	return	r