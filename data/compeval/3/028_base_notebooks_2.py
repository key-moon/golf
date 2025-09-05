def	p(g):
	h,w=len(g),len(g[0]);D={}
	for	r	in	range(h):
		for	c	in	range(w):
			if	g[r][c]!=0:D[g[r][c]]=r
	E=sorted(D.items(),key=lambda	item:item[1]);A,B=E[0][0],E[1][0];C=[[0]*w	for	_	in	range(h)]
	for	r	in	range(5):C[r]=[A]*w	if	r	in[0,2]else[A]+[0]*(w-2)+[A]
	for	r	in	range(5,10):C[r]=[B]*w	if	r	in[7,9]else[B]+[0]*(w-2)+[B]
	return	C