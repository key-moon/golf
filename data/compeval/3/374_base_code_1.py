def	p(g):
	n=len(g);v=[]
	for	i	in	range(n):
		for	j	in	range(n):
			if	g[i][j]==5:
				c=[(i,j)];g[i][j]=0;h=0
				while	h<len(c):
					x,y=c[h];h+=1
					for(a,b)in(1,0),(-1,0),(0,1),(0,-1):
						p,q=x+a,y+b
						if	0<=p<n	and	0<=q<n	and	g[p][q]==5:g[p][q]=0;c+=[(p,q)]
				v+=[c]
	for(k,c)in	enumerate(sorted(v,key=len)):
		for(x,y)in	c:g[x][y]=[2,4,1][k]
	return	g