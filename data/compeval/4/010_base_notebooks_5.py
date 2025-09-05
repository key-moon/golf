def	p(g):
	A,B=len(g),len(g[0])if	g	else	0;C=[[False]*B	for	_	in	range(A)];D=[[0]*B	for	_	in	range(A)];E=1
	def	F(i,j,val):
		if	i<0	or	i>=A	or	j<0	or	j>=B	or	C[i][j]or	g[i][j]!=val:return
		C[i][j]=True;D[i][j]=E
		for(G,H)in[(0,1),(1,0),(0,-1),(-1,0)]:F(i+G,j+H,val)
	for	i	in	range(A):
		for	j	in	range(B):
			if	not	C[i][j]and	g[i][j]!=0:F(i,j,g[i][j]);E+=1
	return	D