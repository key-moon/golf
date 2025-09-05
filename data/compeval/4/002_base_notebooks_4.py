def	p(j):
	B=range;c=len(j);C=[[0]*c	for	A	in	B(c)]
	def	A(k,W):
		if	0<=k<c	and	0<=W<c	and	not	C[k][W]and	j[k][W]==0:C[k][W]=1;[A(k+c,W+B)for(c,B)in[(1,0),(-1,0),(0,1),(0,-1)]]
	[A(B,0)or	A(B,c-1)or	A(0,B)or	A(c-1,B)for	B	in	B(c)];return[[4if	j[A][c]==0and	not	C[A][c]else	j[A][c]for	c	in	B(c)]for	A	in	B(c)]