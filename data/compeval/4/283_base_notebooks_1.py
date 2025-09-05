def	f(g,p,q,a,b,c):
	for	y	in	range(q,b+1):
		for	x	in	range(p,a+1):g[y][x]=c
def	z(g,p,q,a,b):f(g,p,q,a,b,4);f(g,p+1,q+1,a-1,b-1,2);g[q][p]=g[q][a]=g[b][p]=g[b][a]=1
def	p(g):
	h,w=len(g),len(g[0])
	for	i	in	range(h*w):
		x,y=i%w,i//w
		if	g[y][x]==5:
			a,b=x,y
			while	a<w-1and	g[b][a+1]==5:a+=1
			while	b<h-1and	g[b+1][a]==5:b+=1
			z(g,x,y,a,b)
	return	g