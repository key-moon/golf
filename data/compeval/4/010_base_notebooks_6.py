def	p(g):
	h,w=len(g),len(g[0]);c=[[0]*w	for	_	in	range(h)];C=1;v=set()
	for	i	in	range(h):
		for	j	in	range(w):
			if	g[i][j]!=0and(i,j)not	in	v:
				q=[(i,j)];D=[]
				while	q:
					y,x=q.pop(0)
					if(y,x)in	v:continue
					v.add((y,x));D.append((y,x))
					for(E,F)in[(0,1),(1,0),(0,-1),(-1,0)]:
						A,B=y+E,x+F
						if	0<=A<h	and	0<=B<w	and	g[A][B]!=0and(A,B)not	in	v:q.append((A,B))
				for(y,x)in	D:c[y][x]=C
				C=C%9+1
	return	c