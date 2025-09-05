def	p(g):
	C=range;A=len(g);D=[[0]*A	for	B	in	C(A)]
	def	B(i,j):
		if	0<=i<A	and	0<=j<A	and	not	D[i][j]and	g[i][j]==0:D[i][j]=1;[B(i+A,j+C)for(A,C)in[(1,0),(-1,0),(0,1),(0,-1)]]
	[B(C,0)or	B(C,A-1)or	B(0,C)or	B(A-1,C)for	C	in	C(A)];return[[4if	g[B][A]==0and	not	D[B][A]else	g[B][A]for	A	in	C(A)]for	B	in	C(A)]