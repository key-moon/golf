def	p(g,w=range):
	r=[A[:]for	A	in	g];v=set()
	for	i	in	w(len(g)-2):
		for	j	in	w(len(g[0])):
			if	g[i][j]and(i,j)not	in	v:
				c=g[i][j]
				if	all(g[i+k][j]==c	for	k	in	w(3)):
					A=j
					while	A<len(g[0])and	all(g[i+k][A]==c	for	k	in	w(3)):
						for	k	in	w(3):v.add((i+k,A))
						A+=1
					for	x	in	w(j,A):
						if(x-j)%2==1:r[i+1][x]=0
	return	r