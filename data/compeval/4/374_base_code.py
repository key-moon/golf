def	p(g):
	c=[];d=1,0,-1,0,1
	for	i	in	range(10):
		for	j	in	range(10):
			if	g[i][j]==5:
				s=[(i,j)];g[i][j]=0;o=[]
				while	s:
					x,y=s.pop();o.append((x,y))
					for	k	in	range(4):
						A=x+d[k];B=y+d[k+1]
						if	0<=A<10and	0<=B<10and	g[A][B]==5:g[A][B]=0;s.append((A,B))
				c.append(o)
	for(o,v)in	zip(sorted(c,key=len,reverse=True),(1,4,2)):
		for(x,y)in	o:g[x][y]=v
	return	g