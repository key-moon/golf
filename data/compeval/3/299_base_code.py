def	p(g):
	d={}
	for(y,r)in	enumerate(g):
		for(x,v)in	enumerate(r):
			if	v:d.setdefault(v,[]).append((y,x))
	(a,p),(b,q)=d.items()
	if	p[0][0]==p[1][0]:C=a;A=p[0][0];D=b;B=q[0][1]
	else:C=b;A=q[0][0];D=a;B=p[0][1]
	h,w=len(g),len(g[0]);o=[[0]*w	for	_	in	range(h)]
	for	y	in	range(h):o[y][B]=D
	for	x	in	range(w):o[A][x]=C
	o[A][B]=4;return	o