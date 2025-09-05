L=len
R=range
def	p(g):
	g=[r[:]+r[:]for	r	in	g]+[r[:]+r[:]for	r	in	g];h,w=L(g),L(g[0])
	for	r	in	R(h):
		for	c	in	R(w):
			A=g[r][c]
			if	A>0and	A!=8:
				for(i,j)in[[1,1],[-1,-1],[-1,1],[1,-1]]:
					if	i+r>=0and	j+c>=0and	i+r<h	and	j+c<w:
						if	g[i+r][j+c]==0:g[i+r][j+c]=8
	return	g