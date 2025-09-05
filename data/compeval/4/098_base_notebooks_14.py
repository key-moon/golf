def	p(g):
	h,w=len(g),len(g[0]);A=[[0]*w	for	_	in	range(h)]
	for	i	in	range(h):
		for	j	in	range(w):
			if	g[i][j]!=0:
				B=False
				for(E,F)in[(0,1),(1,0),(0,-1),(-1,0)]:
					C,D=i+E,j+F
					if	not(0<=C<h	and	0<=D<w)or	g[C][D]==0:B=True;break
				if	B:A[i][j]=g[i][j]
	return	A