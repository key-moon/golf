def	p(g):
	for	r	in	range(len(g)):
		for	c	in	range(len(g[0])):
			if	g[r][c]==1:g[r][c]=0
	A=[]
	for	i	in	range(len(g)):
		if	sum(g[i])>0:A.append(i)
	g=g[min(A):max(A)+1];A=[]
	for	B	in	g:
		for	i	in	range(len(B)):
			if	B[i]>0:A.append(i)
	g=[B[min(A):max(A)+1]for	B	in	g];return	g