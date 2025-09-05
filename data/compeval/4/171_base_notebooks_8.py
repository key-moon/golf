def	p(grid):
	A=len(grid);B=len(grid[0]);C=[[0for	_	in	range(B)]for	_	in	range(A)]
	for	r	in	range(A):
		for	c	in	range(B):
			if	r==0	or	r==A-1or	c==0	or	c==B-1:C[r][c]=8
			else:C[r][c]=0
	return	C