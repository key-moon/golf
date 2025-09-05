def	p(g,L=len,R=range):
	h,w,x,y,b=L(g),L(g[0]),[],[],[]
	for	r	in	R(h):
		for	c	in	R(w):
			A=g[r][c]
			if	A==2:x+=[c];g[r][c]=0
			if	A==4:y+=[c];g[r][c]=0
			if	A==1:b+=[c]
	for	r	in	R(h):
		for	c	in	R(w):
			if	g[r][c]==1:g[r][c+(min(y)-min(b))]=4;g[r][c+(min(x)-min(b))]=2
	return	g