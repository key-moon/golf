def	p(g):
	for	i	in	range(10):
		for	j	in	range(10):
			s=[(i,j)]
			for(y,x)in	s:
				for	k	in	range(4):
					A=y+7%~k+1;B=x+k+2%~k*2
					if-1<A<10>B>-1and	g[A][B]and(A,B)not	in	s:s.append((A,B))
			if	g[i][j]:g[i][j]=(len(s)==6)+1
	return	g