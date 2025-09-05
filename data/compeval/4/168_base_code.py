def	p(g):
	A,B=len(g),len(g[0])
	for	i	in	range(A):
		for	j	in	range(B):
			x=g[i][j]
			if	x:
				E=F=G=0
				for(C,D)in(1,0),(-1,0),(0,1),(0,-1):
					if	0<=i+C<A	and	0<=j+D<B	and	g[i+C][j+D]==x:E+=C;F+=D;G+=1
				if	G==2:
					t=1
					while	1:
						t+=1;a,b=i+E*t,j+F*t
						if	a<0	or	a>=A	or	b<0	or	b>=B:break
						if	not	g[a][b]:g[a][b]=x
	return	g