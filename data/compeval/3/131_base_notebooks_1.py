t=lambda	g:[[g[y][x]for	y	in	range(len(g))]for	x	in	range(len(g[0]))]
def	p(g):
	h,w=len(g),len(g[0])
	if	w>h:return	t(p(t(g)))
	a,b,c=0,h,0
	for(y,r)in	enumerate(g):
		if	r[0]==2:a=y
		if	any(i==3for	i	in	r):b,c=min(b,y),y
	if	b<a:return	p(g[::-1])[::-1]
	return	g[:a+1]+g[b:c+1]+[[8]*w]+[[0]*w]*(h-a+b-c-3)